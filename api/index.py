import json
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse


class handler(BaseHTTPRequestHandler):
    student_marks = [{"name": "ks2d6", "marks": 27},
                     {"name": "TzkV80", "marks": 84},
                     {"name": "pptVSHJ3Xr", "marks": 37},
                     {"name": "oXiIr", "marks": 51},
                     {"name": "zfM0YvloCd", "marks": 88},
                     {"name": "yQ4InKSAtD", "marks": 40},
                     {"name": "0Eom", "marks": 60},
                     {"name": "MXyFrecar", "marks": 71},
                     {"name": "m", "marks": 60},
                     {"name": "IduyzK",
                      "marks": 88},
                     {"name": "8", "marks": 78},
                     {"name": "zQmBo", "marks": 86},
                     {"name": "1Jy", "marks": 58},
                     {"name": "zl22B", "marks": 73},
                     {"name": "8kw", "marks": 66},
                     {"name": "im9PJ", "marks": 36},
                     {"name": "r", "marks": 50},
                     {"name": "duw", "marks": 38},
                     {"name": "l", "marks": 90},
                     {"name": "h5Tc2Opb", "marks": 44},
                     {"name": "Mt", "marks": 87},
                     {"name": "f5qw", "marks": 28},
                     {"name": "8EOaO", "marks": 91},
                     {"name": "uCQ", "marks": 38},
                     {"name": "csjPc", "marks": 35},
                     {"name": "ts1nvdsasz", "marks": 28},
                     {"name": "79C2fIyh9", "marks": 82},
                     {"name": "6Fz", "marks": 47},
                     {"name": "qzGQ4", "marks": 46},
                     {"name": "J", "marks": 17},
                     {"name": "jdDjHzh", "marks": 28},
                     {"name": "GCcAx7", "marks": 97},
                     {"name": "jmfmcJXzKx", "marks": 57},
                     {"name": "BPub", "marks": 14},
                     {"name": "COCBX", "marks": 19},
                     {"name": "rm", "marks": 18},
                     {"name": "BMvt", "marks": 95},
                     {"name": "xM1wj4", "marks": 12},
                     {"name": "p", "marks": 18},
                     {"name": "2RNP3OL", "marks": 82},
                     {"name": "rxR78Tgrd", "marks": 33},
                     {"name": "XDyx82V8oK", "marks": 34},
                     {"name": "aOrJp", "marks": 44},
                     {"name": "A", "marks": 39},
                     {"name": "6KFuvge", "marks": 49},
                     {"name": "K46sTYtQ", "marks": 75},
                     {"name": "l96oDIPFEg", "marks": 97},
                     {"name": "57yWggK8Lh", "marks": 29},
                     {"name": "PyBPgRR7O", "marks": 44},
                     {"name": "uBtw", "marks": 97},
                     {"name": "x1", "marks": 42},
                     {"name": "Cr", "marks": 77},
                     {"name": "PiQ", "marks": 21},
                     {"name": "qWBlU", "marks": 83},
                     {"name": "tJ5ZNmNaH", "marks": 7},
                     {"name": "bZ39UV", "marks": 21},
                     {"name": "nnSSDhj", "marks": 34},
                     {"name": "FFCcx", "marks": 27},
                     {"name": "6", "marks": 42},
                     {"name": "LHQQpDWG", "marks": 6},
                     {"name": "38mk4", "marks": 78},
                     {"name": "uOG6IV", "marks": 71},
                     {"name": "jiXgrYrvVx", "marks": 54},
                     {"name": "S0q46", "marks": 10},
                     {"name": "Xcbi4kyb", "marks": 92},
                     {"name": "s9w3i", "marks": 76},
                     {"name": "i", "marks": 21},
                     {"name": "dBdG", "marks": 1},
                     {"name": "lz40d", "marks": 1},
                     {"name": "beZbfVLPVT", "marks": 31},
                     {"name": "UEM", "marks": 59},
                     {"name": "Y", "marks": 71},
                     {"name": "fgQjITGrg", "marks": 54},
                     {"name": "FcqMc2K2", "marks": 14},
                     {"name": "CmlLSZh3", "marks": 46},
                     {"name": "7F", "marks": 59},
                     {"name": "Wz", "marks": 46},
                     {"name": "b27Ay", "marks": 55},
                     {"name": "jkOb", "marks": 38},
                     {"name": "v", "marks": 13},
                     {"name": "Q", "marks": 61},
                     {"name": "F", "marks": 8},
                     {"name": "fHzMIStaV", "marks": 95},
                     {"name": "Ml1n", "marks": 10},
                     {"name": "lYF", "marks": 76},
                     {"name": "eKwQqbI2", "marks": 81},
                     {"name": "umG8AEW", "marks": 35},
                     {"name": "av3", "marks": 20},
                     {"name": "4oyO52k5", "marks": 47},
                     {"name": "AUW", "marks": 18},
                     {"name": "B", "marks": 48},
                     {"name": "gt", "marks": 69},
                     {"name": "jco", "marks": 60},
                     {"name": "IOjUeA", "marks": 13},
                     {"name": "V1ehiU5H9", "marks": 52},
                     {"name": "ONUgBE", "marks": 72},
                     {"name": "yR47b", "marks": 41},
                     {"name": "9hIcRTFD8", "marks": 99},
                     {"name": "7SGN", "marks": 82},
                     {"name": "Thm", "marks": 59}]

    def do_GET(self):
        query = parse_qs(urlparse(self.path).query)
        names = query.get("name", [])

        marks = []
        for name in names:
            for student in self.student_marks:
                if student["name"] == name:
                    marks.append(student["marks"])
                    break

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        response = {"marks": marks}
        self.wfile.write(json.dumps(response).encode("utf-8"))

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)

        try:
            received_data = json.loads(post_data)
            name = received_data.get("name")
            marks = received_data.get("marks")

            if not name or marks is None:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(json.dumps(
                    {"error": "Invalid JSON data"}).encode("utf-8"))
                return

            # Check if student exists and update marks
            for student in self.student_marks:
                if student["name"] == name:
                    student["marks"] = marks
                    break
            else:
                self.student_marks.append({"name": name, "marks": marks})

            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods',
                             'POST, GET, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            self.end_headers()

            response = {"message": "Student marks updated successfully",
                        "updated_student": {"name": name, "marks": marks}}
            self.wfile.write(json.dumps(response).encode("utf-8"))

        except json.JSONDecodeError:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(json.dumps(
                {"error": "Invalid JSON format"}).encode("utf-8"))
