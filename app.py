from flask import Flask, request, redirect

app = Flask(__name__)


# =====================================================
# GET /api/hash.php
# =====================================================
@app.route("/api/hash.php", methods=["GET"])
def hash_php():
    return "c966b57c651dc9ff89a2ebdf65d6dfa659f0acbab1f45af25d1597f242c3bdf0"


# =====================================================
# GET /api/auth?datavery=
# =====================================================
@app.route("/api/auth", methods=["GET"])
def auth():
    return "nk0wr0oxw1d5a8n2j49fc26gyinwe6khqf1n1zhwk2ayy3tvv0igf0z435mu"


# =====================================================
# POST /api/active_soft_final_20240605
# =====================================================
@app.route("/api/active_soft_final_20240605", methods=["POST", "GET"])
def active():
    return """MZFjT0A5bkJlYzQjNRVDRM4W8Ro7tJRzYupgHVBJ2tTwkvkJumaNVVkyVnRlVWwzZWtwS1lXUnJTbFZhWWt0UU5URnJWRFpaYzBkRVZGaFhNRVp3WjNwSlVYVlhWbTlIZDNCdkwyRlJRMUkxVEZCRVQyMXpaVzg1ZURaRE16TXdTMVZOTUU0Mk5TOU9NREZRUVZKUVQzWmhRVXBMUkZCeFUzZEtSWGQzUVRWNllURjBNbE5TUW0xd1ZURktaRFZpVlhJelFtcDNWVEJtWW14d1dFcEpWV3BEVDNaV1RqTmplWFYwVG1wUVNsVnBUV3BXU1VoeFlrVlRXRTB2YjNjMWFHWXlRMGxzVUZrd1ZGSnVUMHBRZEhkVFoyWnliVk13TUd4VGFpOTZRMEp3VFZSYU0xaDZRVFE0ZW1OMFdYVTBOWFJ0VTIwNWVXWjBVR3BHVEdsaFFsZElZemxWZFhwQlZFSkJRV3BxVDFacGMxVlNSSGRYYlVwcmRFaHplRzVFUTIwcmRucFNja2RSTW5JMVNVMDJWa3B1U2l0MFlXSmFVRFkzY1hScFF6Rk5RbWRsWkhaT1ZHMVNlVk0yU0UxWVdEWmtXazk2UkROc1VHMXhlRXN5VWpWSFVsSTJkVGhITTFwNWNHcG9VMXA2VkhaVWR6WjBURWhwTlhaeU1YaEtLMGczU0c1U0swWlVRWGNyU0ZwbGNHNWpZbkZGU2xCQ04xTjFMM0ZNZERkMlMwOUlZamMxUmtGUWNtMWpTME4ySzNsSmJHcDRX0hrLXyC3Rkh9tiwBgn8mCha6evOeFffTsZlVlSEZPUVhkSVEbrFG|cbb0c5291e7f628452b9ce7f5e9bda658200df442e9aab3ebf48023887e7097d"""


# =====================================================
# MAIN
# =====================================================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=443)
