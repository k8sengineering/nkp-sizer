from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    workload_clusters = data.get("workload_clusters", 1)
    p2v_ratio = data.get("p2v_ratio", 1.5)
    platform_apps = data.get("platform_apps", [])
    total_vcores = sum(app["cpu"] for app in platform_apps if app["enabled"])
    total_memory = sum(app["memory"] for app in platform_apps if app["enabled"])
    total_storage = sum(app["storage"] for app in platform_apps if app["enabled"])
    effective_cores = total_vcores / p2v_ratio

    return jsonify({
        "total_vcores": total_vcores * workload_clusters,
        "total_memory": total_memory * workload_clusters,
        "total_storage": total_storage * workload_clusters,
        "effective_cores": effective_cores
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

