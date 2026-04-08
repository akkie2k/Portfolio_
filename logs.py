import urllib.request, json
run_id = 24148178045
jobs_url = f'https://api.github.com/repos/akkie2k/Portfolio_/actions/runs/{run_id}/jobs'
req = urllib.request.Request(jobs_url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response:
    jobs = json.loads(response.read().decode())
    for job in jobs.get('jobs', []):
        if job.get('name') == 'deploy':
            job_id = job['id']
            log_url = f'https://api.github.com/repos/akkie2k/Portfolio_/actions/jobs/{job_id}/logs'
            try:
                log_req = urllib.request.Request(log_url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(log_req) as log_response:
                    logs = log_response.read().decode()
                    # Just print the last 50 lines to find the error
                    print("\n".join(logs.split("\n")[-100:]))
            except Exception as e:
                print('Error fetching logs:', e)
