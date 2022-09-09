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
Kaggle's Titanic dataset schema.
"""
from forml.io import dsl


class Titanic(dsl.Schema):
    """Titanic passenger list.

    See Also:
        The original `Titanic competition <https://www.kaggle.com/c/titanic>`_.
    """

    PassengerId = dsl.Field(dsl.Integer())
    """Passenger ID."""

    Survived = dsl.Field(dsl.Integer())
    """Survival.

    :Values:
        * ``0`` = No
        * ``1`` = Yes
    """

    Pclass = dsl.Field(dsl.Integer())
    """Ticket class - proxy for socioeconomic status (SES).

    :Values:
        * ``1`` = first (Upper)
        * ``2`` = second (Middle)
        * ``3`` = third (Lower)
    """

    Name = dsl.Field(dsl.String())
    """Passenger name."""

    Sex = dsl.Field(dsl.String())
    """Sex.

    :Values:
        * ``male``
        * ``female``
    """

    Age = dsl.Field(dsl.Float())
    """Age in years.

    Age is fractional if less than ``1``. If the age is estimated, it is in the form of ``xx.5``.
    """

    SibSp = dsl.Field(dsl.Integer())
    """Number of siblings / spouses aboard the Titanic.

    The dataset defines family relations in this way:

        * Sibling: brother, sister, stepbrother, stepsister
        * Spouse: husband, wife (mistresses and fiances were ignored)
    """

    Parch = dsl.Field(dsl.Integer())
    """Number of parents / children aboard the Titanic.

    The dataset defines family relations in this way:

        * Parent: mother, father
        * Child: daughter, son, stepdaughter, stepson

    Some children traveled only with a nanny, therefore ``parch=0`` for them.
    """

    Ticket = dsl.Field(dsl.String())
    """Ticket number."""

    Fare = dsl.Field(dsl.Float())
    """Passenger fare."""

    Cabin = dsl.Field(dsl.String())
    """Cabin number."""

    Embarked = dsl.Field(dsl.String())
    """Port of Embarkation.

    :Values:
        * ``C`` = Cherbourg
        * ``Q`` = Queenstown
        * ``S`` = Southampton
    """
