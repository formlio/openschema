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

""" `Sklearn flavour
<https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_boston.html>`_ of the
*Boston house prices* dataset schema.

It differs from the `original UCIML <https://archive.ics.uci.edu/ml/machine-learning-databases/housing/>`_ version
having few data point fixes.
"""
from forml.io.dsl import struct
from forml.io.dsl.struct import kind


class Prices(struct.Schema):
    """Boston house prices dataset.

    :Number of Instances: 506
    :Number of Attributes: 13 numeric/categorical predictive. Median Value (attribute 14) is usually the target.
    :Missing Attribute Values: None
    :Creator: Harrison, D. and Rubinfeld, D.L.Z
    """

    CRIM = struct.Field(kind.Float())
    """float: Per capita crime rate by town."""

    ZN = struct.Field(kind.Float())
    """float: Proportion of residential land zoned for lots over 25,000 sq.ft."""

    INDUS = struct.Field(kind.Float())
    """float: Proportion of non-retail business acres per town."""

    CHAS = struct.Field(kind.Float())
    """float: Charles River dummy variable.

    :Values:
        * 1 = tract bounds river
        * 0 = otherwise
    """

    NOX = struct.Field(kind.Float())
    """float: Nitric oxides concentration (parts per 10 million)."""

    RM = struct.Field(kind.Float())
    """float: Average number of rooms per dwelling."""

    AGE = struct.Field(kind.Float())
    """float: Proportion of owner-occupied units built prior to 1940."""

    DIS = struct.Field(kind.Float())
    """float: Weighted distances to five Boston employment centres."""

    RAD = struct.Field(kind.Float())
    """float: Index of accessibility to radial highways."""

    TAX = struct.Field(kind.Float())
    """float: Full-value property-tax rate per $10,000."""

    PTRATIO = struct.Field(kind.Float())
    """float: Pupil-teacher ratio by town."""

    B = struct.Field(kind.Float())
    """float: 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town."""

    LSTAT = struct.Field(kind.Float())
    """float: % lower status of the population."""

    MEDV = struct.Field(kind.Float())
    """float: Median value of owner-occupied homes in $1000's."""
