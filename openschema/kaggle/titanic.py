# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""
`Kaggle's Titanic <https://www.kaggle.com/c/titanic>`_ dataset schema.
"""
from forml.io.dsl import struct
from forml.io.dsl.struct import kind


class Passenger(struct.Schema):
    """Titanic passenger list."""

    PassengerId = struct.Field(kind.Integer())
    """int: Passenger ID."""

    Survived = struct.Field(kind.Integer())
    """int: Survival.

    :Values:
        * 0 = No.
        * 1 = Yes.
    """

    Pclass = struct.Field(kind.Integer())
    """int: Ticket class - proxy for socio-economic status (SES).

    :Values:
        * 1 = 1st (Upper)
        * 2 = 2nd (Middle)
        * 3 = 3rd (Lower)
    """

    Name = struct.Field(kind.String())
    """str: Passenger name."""

    Sex = struct.Field(kind.String())
    """str: Sex.

    :Values:
        * male
        * female
    """

    Age = struct.Field(kind.Float())
    """float: Age in years.

    Age is fractional if less than 1. If the age is estimated, is it in the form of xx.5.
    """

    SibSp = struct.Field(kind.Integer())
    """int: Number of siblings / spouses aboard the Titanic.

    The dataset defines family relations in this way:

        * Sibling: brother, sister, stepbrother, stepsister
        * Spouse: husband, wife (mistresses and fiancés were ignored)
    """

    Parch = struct.Field(kind.Integer())
    """int: Number of parents / children aboard the Titanic.

    The dataset defines family relations in this way:

        * Parent: mother, father
        * Child: daughter, son, stepdaughter, stepson

    Some children travelled only with a nanny, therefore parch=0 for them.
    """

    Ticket = struct.Field(kind.Integer())
    """int: Ticket number."""

    Fare = struct.Field(kind.Float())
    """float: Passenger fare."""

    Cabin = struct.Field(kind.String())
    """Cabin number."""

    Embarked = struct.Field(kind.String())
    """Port of Embarkation.

    :Values:
        * C = Cherbourg
        * Q = Queenstown
        * S = Southampton
    """
