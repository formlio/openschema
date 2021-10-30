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

"""`Sklearn flavour
<https://scikit-learn.org/stable/datasets/index.html#iris-plants-dataset>`_ of the
*Iris Plants* dataset schema.

It differs from the `original UCIML <https://archive.ics.uci.edu/ml/datasets/Iris>`_ version in the ``Class`` type plus
there are few data point fixes.
"""
from forml.io import dsl


class Iris(dsl.Schema):
    """Iris Plants Database.

    :Number of Instances: 150 (50 in each of three classes)
    :Number of Attributes: 4 numeric, predictive attributes and the class
    :Summary Statistics:

    ============== ==== ==== ======= ===== ====================
       Feature      Min  Max   Mean    SD   Class Correlation
    ============== ==== ==== ======= ===== ====================
    sepal length    4.3  7.9   5.84   0.83    0.7826
    sepal width     2.0  4.4   3.05   0.43   -0.4194
    petal length    1.0  6.9   3.76   1.76    0.9490  (high!)
    petal width     0.1  2.5   1.20   0.76    0.9565  (high!)
    ============== ==== ==== ======= ===== ====================

    :Missing Attribute Values: None
    :Class Distribution: 33.3% for each of 3 classes.
    :Creator: R.A. Fisher
    :Donor: Michael Marshall (MARSHALL%PLU@io.arc.nasa.gov)
    :Date: July, 1988
    """

    SepalLength = dsl.Field(dsl.Float())
    """float: Sepal length in cm."""

    SepalWidth = dsl.Field(dsl.Float())
    """float: Sepal width in cm."""

    PetalLength = dsl.Field(dsl.Float())
    """float: Petal length in cm."""

    PetalWidth = dsl.Field(dsl.Float())
    """float: Petal width in cm."""

    Class = dsl.Field(dsl.Integer())
    """int: Class.

    :Values:
        * 0 = setosa
        * 1 = versicolor
        * 2 = virginica
    """
