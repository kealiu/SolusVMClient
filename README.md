# SolusVMClient
The SolusVM API Client SDK

## Example

```python
# init client for your VPS
client = SolusVMClient('http://cpanel.solusvm.com:5656', 'MY-API-KEY', 'myapihashhere')

# check the VPS information
client.info()

# check the VPS status
client.status

# boot the VPS
client.boot()

# reboot the VPS
client.reboot()

# shutdown the VPS
client.shutdown()

```
