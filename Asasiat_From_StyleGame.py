import base64
de="aW1wb3J0IG9zCgpkZWYgbWVudSgpOgogICAgb3Muc3lzdGVtKCJjbGVhciIpCiAgICBwcmludCgiIiIgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgClwwMzNbMTszNG1fX19fXyBfICAgICAgICAgXyAgICAgICBfX19fXwogIC8gX19fX3wgfCAgICAgICB8IHwgICAgIC8gX19fX3wKIHwgKF9fXyB8IHxfIF8gICBffCB8IF9fX3wgfCAgX18gIF9fIF8gXyBfXyBfX18gICBfX18KICBcX19fIFx8IF9ffCB8IHwgfCB8LyBfIFwgfCB8XyB8LyBfYCB8ICBfIGAgXyBcIC8gXyBcCiAgX19fXykgfCB8X3wgfF98IHwgfCAgX18vIHxfX3wgfCAoX3wgfCB8IHwgfCB8IHwgIF9fLwogfF9fX19fLyBcX198XF9fLCB8X3xcX19ffFxfX19fX3xcX18sX3xffCB8X3wgfF98XF9fX3wKICAgICAgICAgICAgICBfXy8gfAogICAgICAgICAgICAgfF9fXy8KICAgICAgICAgICAgIAogICAgICAgICAgXDAzM1sxOzM3bSgnZm9sbG93IG15IG9uIHRsZWdyYW0gQFN0eWxlR2FtZTEnKQogICAgICAgICAgCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS1DaG9vc2UgYSBudW1iZXItLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQpfX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fXwoxLlRhc2JpdCBBc2FzaWF0IEFsIFRlcm11eApfX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fXwowMC5FeGl0IApfX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fXyIiIikKCmxvb3AgPSBUcnVlCgp3aGlsZSBsb29wOgogICAgbWVudSgpCiAgICB3aGF0ID0gaW5wdXQoIiNTdHlsZUdhbWU6ICIpCiAgICBpZiB3aGF0ID09ICIxIjoKICAgICAgICBwcmludCgiXDAzM1sxOzMybT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09IikKICAgICAgICAKICAgICAgICBobSA9IGlucHV0KCJbP10gRG8geW91IHdhbnQgdG8gY29udGludWU/ICh5L24pOiAiKQogICAgICAgIHByaW50KCI9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PSIpCiAgICAgICAgaWYgaG0gPT0gInkiOgogICAgICAgICAgICBwcmludCgiXDAzM1sxOzM1bT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09IikKICAgICAgICAgICAgcHJpbnQoIlsrXSBQbGVhc2UgcHV0IHlvdXIgcGhvbmUgZHdvbiAiKQogICAgICAgICAgICBwcmludCgiQmVjYXVzZSB0aGlzIHdpbGwgdGFrZSBhIGxvbmcgdGltZS4iKQogICAgICAgICAgICBwcmludCgiXDAzM1sxOzMzbT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09IikgCiAgICAgICAgICAgIG9zLnN5c3RlbSgiYXB0LWdldCB1cGRhdGUgLXkiKQogICAgICAgICAgICBvcy5zeXN0ZW0oImFwdC1nZXQgdXBncmFkZSAteSIpCiAgICAgICAgICAgIG9zLnN5c3RlbSgiYXB0LWdldCBpbnN0YWxsIHB5dGhvbiAteSIpCiAgICAgICAgICAgIG9zLnN5c3RlbSgiYXB0LWdldCBpbnN0YWxsIHB5dGhvbjIgLXkiKQogICAgICAgICAgICBvcy5zeXN0ZW0oImFwdC1nZXQgaW5zdGFsbCBweXRob24zIC15IikKICAgICAgICAgICAgb3Muc3lzdGVtKCJhcHQtZ2V0IGluc3RhbGwgcnVieSAteSIpCiAgICAgICAgICAgIG9zLnN5c3RlbSgiYXB0LWdldCBpbnN0YWxsIGdpdCAteSAgICAgIikKICAgICAgICAgICAgb3Muc3lzdGVtKCJhcHQtZ2V0IGluc3RhbGwgcGhwIC15IikKICAgICAgICAgICAgb3Muc3lzdGVtKCJhcHQtZ2V0IGluc3RhbGwgbmFubyAteSIpCiAgICAgICAgICAgIG9zLnN5c3RlbSgiYXB0LWdldCBpbnN0YWxsIG5tYXAgLXkiKQogICAgICAgICAgICBvcy5zeXN0ZW0oImFwdC1nZXQgaW5zdGFsbCBwZXJsIC15IikKICAgICAgICAgICAgb3Muc3lzdGVtKCJ0ZXJtdXgtc2V0dXAtc3RvcmFnZSAteSIpCiAgICAgICAgICAgIG9zLnN5c3RlbSgiYXB0LWdldCBpbnN0YWxsIGdvbGFuZyAteSIpCiAgICAgICAgICAgIG9zLnN5c3RlbSgiYXB0LWdldCBpbnN0YWxsIGhvc3QgLXkiKQogICAgICAgICAgICBvcy5zeXN0ZW0oImFwdC1nZXQgaW5zdGFsbCBoYXZpaiAteSIpCiAgICAgICAgICAgIG9zLnN5c3RlbSgiYXB0LWdldCBpbnN0YWxsIGh5ZHJhIC15IikKICAgICAgICAgICAgb3Muc3lzdGVtKCJhcHQgaW5zdGFsbCB3aXJlc2hhcmsgLXkiKQogICAgICAgICAgICBvcy5zeXN0ZW0oImFwdC1nZXQgaW5zdGFsbCBjbWF0cml4IC15IikKICAgICAgICAgICAgb3Muc3lzdGVtKCJhcHItZ2V0IGluc3RhbGwgZmlnbGV0IC15IikKICAgICAgICAgICAgb3Muc3lzdGVtKCJhcHQtZ2V0IGluc3RhbGwgd2dldCAteSIpCiAgICAgICAgICAgIG9zLnN5c3RlbSgiYXB0LWdldCBpbnN0YWxsIHdnZXQgLXkiKQogICAgICAgICAgICBvcy5zeXN0ZW0oImFwdC1nZXQgaW5zdGFsbCBweXRob24yIC15IikKICAgICAgICAgICAgb3Muc3lzdGVtKCJhcHQtZ2VnIGluc3RhbGwgcHl0aG9uMi1kZXYgLXkiKQogICAgICAgICAgICBvcy5zeXN0ZW0oImFwdCBpbnN0YWxsIHdpcmVzaGFyayAteSIpCiAgICAgICAgICAgIG9zLnN5c3RlbSgiYXB0LWdldCBpbnN0YWxsIGNvd3NheSAteSIpCiAgICAgICAgICAgIG9zLnN5c3RlbSgiYXB0LWdldCBpbnN0YWxsIHRvaWxldCAteSIpCiAgICAgICAgICAgIG9zLnN5c3RlbSgiYXB0LWdldCBpbnN0YWxsIGN1cmxpbnN0YWxsIHdnZXRyYyAteSIpCiAgICAgICAgICAgIG9zLnN5c3RlbSgiYXB0LWdldCBpbnN0YWxsIHJ1YnkgLXkiKQogICAgICAgICAgICBvcy5zeXN0ZW0oImFwdC1nZXQgaW5zdGFsbCBoZWxwIC15IikKICAgICAgICAgICAgb3Muc3lzdGVtKCJhcHQtZ2V0IGluc3RhbGwgbmV0LXRvb2xzIC15IikKICAgICAgICAgICAgb3Muc3lzdGVtKCJhcHQtZ2V0IGluc3RhbGwgdzNtIC15IikKICAgICAgICAgICAgb3Muc3lzdGVtKCJhcHQtZ2V0IGluc3RhbGwgdW5yYXIgLXkgIikKICAgICAgICAgICAgb3Muc3lzdGVtKCJhcHQtZ2V0IGluc3RhbGwgY2xhbmcgLXkiKQogICAgICAgICAgICBvcy5zeXN0ZW0oImFwdC1nZXQgaW5zdGFsbCBvcGVuc3NoIC15IikKICAgICAgICAgICAgb3Muc3lzdGVtKCJhcHQtZ2V0IGluc3RhbGwgdG9yIC15IikKICAgICAgICAgICAgb3Muc3lzdGVtKCJhcHQtZ2V0IGluc3RhbGwgdGFyIC15IikKICAgICAgICAgICAgb3Muc3lzdGVtKCJhcHQtZ2V0IGluc3RhbGwgemlwIC15IikKICAgICAgICAgICAgb3Muc3lzdGVtKCJhcHQtZ2V0IGluc3RhbGwgcHJvb3QgLXkiKQogICAgICAgICAgICBvcy5zeXN0ZW0oInBpcDIgaW5zdGFsbCB3Z2V0IC15IikKICAgICAgICAgICAgb3Muc3lzdGVtKCJwaXAyIGluc3RhbGwgcmVxdWVzdHMgLXkiKQogICAgICAgICAgICBvcy5zeXN0ZW0oImdlbSBpbnN0YWxsIGxvbGNhdCAteSIpCiAgICAgICAgICAgIG9zLnN5c3RlbSgiYXB0IHVwZGF0ZSAteSAmJiBhcHQgdXBncmFkZSAteSIpCiAgICAgICAgICAgIG9zLnN5c3RlbSgiY2xlYXIiKSAgICAgICAgICAgIAogICAgICAgICAgICBwcmludCgiXDAzM1sxOzMybT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PSIpCiAgICAgICAgICAgIHByaW50KCJbK10gdGFtIHRzYmV0IEFsYXNhc2lhdCkiKQogICAgICAgICAgICBwcmludCgiPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09IikKICAgICAgICAgICAgcm1lbnUgPSBpbnB1dCgiWz9dIEJhY2sgdG8gTWVudT8gKHkvbik6ICIpCiAgICAgICAgICAgIGlmIHJtZW51ID09ICJ5IjoKICAgICAgICAgICAgICAgIGltcG9ydCBvcwogICAgICAgICAgICAgICAgb3Muc3lzdGVtKCJjbGVhciIpCiAgICAgICAgICAgICAgICBtZW51KCkKICAgICAgICAgICAgZWxzZToKICAgICAgICAgICAgICAgIGJyZWFrCiAgICBlbGlmIHdoYXQgPT0gIjAwIjoKICAgICAgICBwcmludCgiXDAzM1sxOzMxbUJheS4iKQogICAgICAgIGJyZWFrCgoKCgoK"
x=base64.b64decode(de)
d=x.decode("utf-8")

g=compile(d,"","exec")
exec(g)
