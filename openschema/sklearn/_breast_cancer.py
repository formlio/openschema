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
<https://scikit-learn.org/stable/datasets/index.html#breast-cancer-wisconsin-diagnostic-dataset>`_ of the
*Breast cancer* dataset schema.

It is the copy of the `original UCIML <https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic)>`_
version.
"""
from forml.io import dsl


class BreastCancer(dsl.Schema):
    """Breast cancer wisconsin (diagnostic) dataset.

    :Number of Instances: 569
    :Number of Attributes: 30 numeric, predictive attributes and the class
    :Attribute Information:

        The mean, standard error, and "worst" or largest (mean of the three
        largest values) of these features were computed for each image,
        resulting in 30 features.  For instance, field 3 is Mean Radius, field
        13 is Radius SE, field 23 is Worst Radius.

    :Summary Statistics:

    ===================================== ====== ======
     Feature                               Min    Max
    ===================================== ====== ======
    radius (mean):                        6.981  28.11
    texture (mean):                       9.71   39.28
    perimeter (mean):                     43.79  188.5
    area (mean):                          143.5  2501.0
    smoothness (mean):                    0.053  0.163
    compactness (mean):                   0.019  0.345
    concavity (mean):                     0.0    0.427
    concave points (mean):                0.0    0.201
    symmetry (mean):                      0.106  0.304
    fractal dimension (mean):             0.05   0.097
    radius (standard error):              0.112  2.873
    texture (standard error):             0.36   4.885
    perimeter (standard error):           0.757  21.98
    area (standard error):                6.802  542.2
    smoothness (standard error):          0.002  0.031
    compactness (standard error):         0.002  0.135
    concavity (standard error):           0.0    0.396
    concave points (standard error):      0.0    0.053
    symmetry (standard error):            0.008  0.079
    fractal dimension (standard error):   0.001  0.03
    radius (worst):                       7.93   36.04
    texture (worst):                      12.02  49.54
    perimeter (worst):                    50.41  251.2
    area (worst):                         185.2  4254.0
    smoothness (worst):                   0.071  0.223
    compactness (worst):                  0.027  1.058
    concavity (worst):                    0.0    1.252
    concave points (worst):               0.0    0.291
    symmetry (worst):                     0.156  0.664
    fractal dimension (worst):            0.055  0.208
    ===================================== ====== ======

    :Missing Attribute Values: None
    :Class Distribution: 212 - Malignant, 357 - Benign
    :Creator:  Dr. William H. Wolberg, W. Nick Street, Olvi L. Mangasarian
    :Donor: Nick Street
    :Date: November, 1995
    """

    mean_radius = dsl.Field(dsl.Float())
    """float: Mean of distances from center to points on the perimeter (mean)."""

    mean_texture = dsl.Field(dsl.Float())
    """float: Standard deviation of gray-scale values (mean)."""

    mean_perimeter = dsl.Field(dsl.Float())
    """float: Perimeter (mean)."""

    mean_area = dsl.Field(dsl.Float())
    """float: Area (mean)."""

    mean_smoothness = dsl.Field(dsl.Float())
    """float: Local variation in radius lengths (mean)."""

    mean_compactness = dsl.Field(dsl.Float())
    """float: perimeter^2 / area - 1.0 (mean)."""

    mean_concavity = dsl.Field(dsl.Float())
    """float: Severity of concave portions of the contour (mean)."""

    mean_concave_points = dsl.Field(dsl.Float())
    """float: Number of concave portions of the contour (mean)."""

    mean_symmetry = dsl.Field(dsl.Float())
    """float: Symmetry (mean)."""

    mean_fractal_dimension = dsl.Field(dsl.Float())
    """float: "coastline approximation" - 1 (mean)."""

    radius_error = dsl.Field(dsl.Float())
    """float: Mean of distances from center to points on the perimeter (standard error)."""

    texture_error = dsl.Field(dsl.Float())
    """float: Standard deviation of gray-scale values (standard error)."""

    perimeter_error = dsl.Field(dsl.Float())
    """float: Perimeter (standard error)."""

    area_error = dsl.Field(dsl.Float())
    """float: Area (standard error)."""

    smoothness_error = dsl.Field(dsl.Float())
    """float: Local variation in radius lengths (standard error)."""

    compactness_error = dsl.Field(dsl.Float())
    """float: perimeter^2 / area - 1.0 (standard error)."""

    concavity_error = dsl.Field(dsl.Float())
    """float: Severity of concave portions of the contour (standard error)."""

    concave_points_error = dsl.Field(dsl.Float())
    """float: Number of concave portions of the contour (standard error)."""

    symmetry_error = dsl.Field(dsl.Float())
    """float: Symmetry (standard error)."""

    fractal_dimension_error = dsl.Field(dsl.Float())
    """float: "coastline approximation" - 1 (standard error)."""

    worst_radius = dsl.Field(dsl.Float())
    """float: Mean of distances from center to points on the perimeter (worst)."""

    worst_texture = dsl.Field(dsl.Float())
    """float: Standard deviation of gray-scale values (worst)."""

    worst_perimeter = dsl.Field(dsl.Float())
    """float: Perimeter (worst)."""

    worst_area = dsl.Field(dsl.Float())
    """float: Area (worst)."""

    worst_smoothness = dsl.Field(dsl.Float())
    """float: Local variation in radius lengths (worst)."""

    worst_compactness = dsl.Field(dsl.Float())
    """float: perimeter^2 / area - 1.0 (worst)."""

    worst_concavity = dsl.Field(dsl.Float())
    """float: Severity of concave portions of the contour (worst)."""

    worst_concave_points = dsl.Field(dsl.Float())
    """float: Number of concave portions of the contour (worst)."""

    worst_symmetry = dsl.Field(dsl.Float())
    """float: Symmetry (worst)."""

    worst_fractal_dimension = dsl.Field(dsl.Float())
    """float: "coastline approximation" - 1 (worst)."""

    diagnosis = dsl.Field(dsl.String())
    """str: Diagnosis class.

    :Values:
        * M = malignant
        * B = benign
    """
