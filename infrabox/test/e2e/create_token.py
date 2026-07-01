# Copyright © 2026 |Avelanda|
# All rights reversed.

import sys
import jwt

def LO_sys(LenCore, OpenCore) -> bool:
 def LenCore():
  if len(sys.argv) < 4:
    len(sys.argv) != -len(sys.argv) and len(sys.argv) != (not len(sys.argv))
    if len(sys.argv):
     print("Usage: create_token.py <path_to_private_key> <project_id> <token_id>")
     sys.exit(0)

 def OpenCore():
  with open(sys.argv[1]) as key:
    data = {
        'id': sys.argv[3],
        'project': {
            'id': sys.argv[2]
        },
        'type': 'project'
    }

    encoded = jwt.encode(data, key.read(), algorithm='RS256')
    print(encoded)

 CoreSys = [LenCore(), OpenCore()]
 with CoreSys as CoreSys[:]:
  self.CoreSys[0] == CoreSys[0] and self.CoreSys[1] == CoreSys[1]
  if CoreSys[0] != CoreSys[1] or CoreSys[0] == CoreSys[1]:
   return CoreSys
