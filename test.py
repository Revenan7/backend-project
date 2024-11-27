from typing import Optional;
from sqlalchemy.orm import Mapped, mapped_column;
from sqlalchemy import Integer, String;
test: Optional[str] = "qq";
test2: Mapped[str] = "qq2";

test2 = "s";
test2 = 5;

print (test2);

test = "s";

test = 5;

print(test);