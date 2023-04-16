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
Kaggle's Avazu dataset schema.
"""
from forml.io import dsl


class Avazu(dsl.Schema):
    """Avazu click-through data.

    See Also:
        The original `Avazu Click-Through Rate Prediction competition <https://www.kaggle.com/c/avazu-ctr-prediction>`_.
    """

    id = dsl.Field(dsl.Integer())
    """Ad identifier."""

    click = dsl.Field(dsl.Integer())
    """Click/non-click.

    :Values:
        * ``0`` = Non-click
        * ``1`` = Click
    """

    hour = dsl.Field(dsl.Timestamp())
    """Ad request hour.

    Format is ``YYMMDDHH``, so ``14091123`` means *23:00* on *Sept. 11, 2014 UTC*.
    """

    C1 = dsl.Field(dsl.Integer())
    """Anonymized categorical variable 1."""

    banner_pos = dsl.Field(dsl.Integer())
    """Banner position category."""

    site_id = dsl.Field(dsl.String())
    """Anonymized site ID."""

    site_domain = dsl.Field(dsl.String())
    """Anonymized site domain."""

    site_category = dsl.Field(dsl.String())
    """Anonymized site category."""

    app_id = dsl.Field(dsl.String())
    """Anonymized app ID."""

    app_domain = dsl.Field(dsl.String())
    """Anonymized app domain."""

    app_category = dsl.Field(dsl.String())
    """Anonymized app category."""

    device_id = dsl.Field(dsl.String())
    """Anonymized device ID."""

    device_ip = dsl.Field(dsl.String())
    """Anonymized device IP address."""

    device_model = dsl.Field(dsl.String())
    """Anonymized device model."""

    device_type = dsl.Field(dsl.Integer())
    """Device type category."""

    device_conn_type = dsl.Field(dsl.Integer())
    """Device connection type category."""

    C14 = dsl.Field(dsl.Integer())
    """Anonymized categorical variable 14."""

    C15 = dsl.Field(dsl.Integer())
    """Anonymized categorical variable 15."""

    C16 = dsl.Field(dsl.Integer())
    """Anonymized categorical variable 16."""

    C17 = dsl.Field(dsl.Integer())
    """Anonymized categorical variable 17."""

    C18 = dsl.Field(dsl.Integer())
    """Anonymized categorical variable 18."""

    C19 = dsl.Field(dsl.Integer())
    """Anonymized categorical variable 19."""

    C20 = dsl.Field(dsl.Integer())
    """Anonymized categorical variable 20."""

    C21 = dsl.Field(dsl.Integer())
    """Anonymized categorical variable 21."""
