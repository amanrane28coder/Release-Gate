# Shipping guide (demo service)

Rules the Release Gate checks, in plain language:

1. No hard-coded secrets. No AWS-style keys, no `api_key = "..."`, no `password = "..."` in code.
2. No `TODO: ship` markers left in code. Finish it or remove it before shipping.
3. All tests must pass. A failing test blocks the release, whatever else looks good.
4. The gate recommends only. It never approves, merges, or deploys.
   A human posts approve/reject in the Switch room. Only the exclusive
   release-manager role may log that decision.
