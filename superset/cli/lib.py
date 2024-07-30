import logging

logger = logging.getLogger(__name__)


def normalize_token(token_name: str) -> str:
    """
        As of click>=7, underscores in function names are replaced by dashes.
        To avoid the need to rename all cli functions, e.g. load_examples to
        load-examples, this function is used to convert dashes back to
        underscores.

        :param token_name: token name possibly containing dashes
        :return: token name where dashes are replaced with underscores
    """
    return token_name.replace("_", "-")