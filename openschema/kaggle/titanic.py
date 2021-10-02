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
from forml.io import dsl


class Passenger(dsl.Schema):
    """Titanic passenger list."""

    PassengerId = dsl.Field(dsl.Integer())
    """int: Passenger ID."""

    Survived = dsl.Field(dsl.Integer())
    """int: Survival.

    :Values:
        * 0 = No.
        * 1 = Yes.
    """

    Pclass = dsl.Field(dsl.Integer())
    """int: Ticket class - proxy for socio-economic status (SES).

    :Values:
        * 1 = 1st (Upper)
        * 2 = 2nd (Middle)
        * 3 = 3rd (Lower)
    """

    Name = dsl.Field(dsl.String())
    """str: Passenger name."""

    Sex = dsl.Field(dsl.String())
    """str: Sex.

    :Values:
        * male
        * female
    """

    Age = dsl.Field(dsl.Float())
    """float: Age in years.

    Age is fractional if less than 1. If the age is estimated, is it in the form of xx.5.
    """

    SibSp = dsl.Field(dsl.Integer())
    """int: Number of siblings / spouses aboard the Titanic.

    The dataset defines family relations in this way:

        * Sibling: brother, sister, stepbrother, stepsister
        * Spouse: husband, wife (mistresses and fiancés were ignored)
    """

    Parch = dsl.Field(dsl.Integer())
    """int: Number of parents / children aboard the Titanic.

    The dataset defines family relations in this way:

        * Parent: mother, father
        * Child: daughter, son, stepdaughter, stepson

    Some children travelled only with a nanny, therefore parch=0 for them.
    """

    Ticket = dsl.Field(dsl.Integer())
    """int: Ticket number."""

    Fare = dsl.Field(dsl.Float())
    """float: Passenger fare."""

    Cabin = dsl.Field(dsl.String())
    """Cabin number."""

    Embarked = dsl.Field(dsl.String())
    """Port of Embarkation.

    :Values:
        * C = Cherbourg
        * Q = Queenstown
        * S = Southampton
    """
