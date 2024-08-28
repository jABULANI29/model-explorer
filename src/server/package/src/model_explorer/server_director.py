# Copyright 2024 The AI Edge Model Explorer Authors.
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
# ==============================================================================

import requests

from .config import ModelExplorerConfig


class ServerDirector:
  """A class to ask an exsiting ME server to do stuff."""

  def __init__(self, config: ModelExplorerConfig):
    self.config = config

  def start(self):
    # TODO: add logic to convert pytorch to json and put it in data, and from
    # the other end, replace that data with the config in the running server.
    #
    # also for json.

    # Update config in the running server.
    data = self.config.get_transferrable_data()
    requests.post(f'http://{self.config.reuse_server_host}:{self.config.reuse_server_port}/apipost/v1/update_config',
                  json=data)
