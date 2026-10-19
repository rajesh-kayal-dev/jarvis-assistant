
import re
from dataclasses import dataclass
from enum import Enum


class CommandType(Enum):
    CONVERSATION = "conversation"
    OPEN_WEBSITE = "open_website"
    PLAY_MUSIC = "play_music"
    NEWS = "news"
    AI = "ai"


@dataclass(frozen=True)
class ParsedCommand:
    type: CommandType
    argument: str = ""


class CommandRouter:
    OPEN_PATTERN = re.compile(
        r"^(?:(?:can|could|would) you\s+|please\s+)*"
        r"open\s+(.+?)[?.!]*$",
        re.IGNORECASE,
    )

    PLAY_PATTERN = re.compile(
        r"^(?:(?:can|could|would) you\s+|please\s+)*"
        r"play\s+(.+?)[?.!]*$",
        re.IGNORECASE,
    )

    PREFIX_PATTERN = re.compile(
        r"^(?:hey\s+)?jarvis[:,]?\s*",
        re.IGNORECASE,
    )

    FILLER_PATTERN = re.compile(
        r"\s+(?:for me|please)$",
        re.IGNORECASE,
    )

    def route(self, message: str) -> ParsedCommand:
        message = message.strip()

        if not message:
            return ParsedCommand(CommandType.CONVERSATION)

        message = self.PREFIX_PATTERN.sub("", message).strip()

        open_match = self.OPEN_PATTERN.match(message)
        if open_match:
            return ParsedCommand(
                CommandType.OPEN_WEBSITE,
                self._clean_argument(open_match.group(1)),
            )

        play_match = self.PLAY_PATTERN.match(message)
        if play_match:
            return ParsedCommand(
                CommandType.PLAY_MUSIC,
                self._clean_argument(play_match.group(1)),
            )

        if re.search(r"\bnews\b", message, re.IGNORECASE):
            return ParsedCommand(CommandType.NEWS)

        return ParsedCommand(CommandType.AI)

    @classmethod
    def _clean_argument(cls, argument: str) -> str:
        argument = argument.strip().rstrip("?.!,")
        argument = cls.FILLER_PATTERN.sub("", argument)
        return argument.strip()
