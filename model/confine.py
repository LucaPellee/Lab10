from dataclasses import dataclass

from model.country import Country


@dataclass
class Confine:
    cnt1: Country
    cnt2: Country