
import rlp
from eth.rlp.sedes import uint64
from .deposit_input import DepositInput
from eth.beacon.typing import (
    Timestamp,
    Gwei,
)


class DepositData(rlp.Serializable):
    """
    Not in spec, this is for fields in Deposit
    """
    fields = [
        ('deposit_input', DepositInput),
        # Value in Gwei
        ('value', uint64),
        # Timestamp from deposit contract
        ('timestamp', uint64),
    ]

    def __init__(self,
                 deposit_input: DepositInput,
                 value: Gwei,
                 timestamp: Timestamp) -> None:

        super().__init__(
            deposit_input,
            value,
            timestamp,
        )
