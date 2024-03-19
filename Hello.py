# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger
import pandas as pd
LOGGER = get_logger(__name__)

def run():
    st.set_page_config(layout="wide")
    st.write("Data Dictionary (Data from CDC PLACES, EPA SLD, USGS Building Footprint)")
    url1 = "https://chronicdata.cdc.gov/500-Cities-Places/PLACES-Census-Tract-Data-GIS-Friendly-Format-2023-/yjkw-uj5s"
    st.write("CDC PLACES - Go to metadata [source](%s)"%url1)
    df1 = pd.read_csv("CDC_metadata.csv")
    st.dataframe(data=df1,use_container_width=True)
    url2 = "https://www.epa.gov/system/files/documents/2023-10/epa_sld_3.0_technicaldocumentationuserguide_may2021_0.pdf"
    st.write("EPA SLD - Go to metadata [source](%s)"%url2)
    df2 = pd.read_csv("EPA_metadata.csv")
    st.dataframe(data=df2,use_container_width=True)
    url3 = "https://www.sciencebase.gov/catalog/file/get/5775469ce4b07dd077c7088a?f=__disk__48%2F5f%2Fbe%2F485fbece9f077c7271822e787e45a505ede77d02&transform=1&allowOpen=true"
    st.write("USGS Building Footprint - Go to metadata [source](%s)"%url3)
    df3 = pd.read_csv("USGSBFP_metadata.csv")
    st.dataframe(data=df3,use_container_width=True)
if __name__ == "__main__":
    run()
