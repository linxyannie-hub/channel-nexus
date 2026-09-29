"""Run Channel Nexus locally with Python's standard library."""

from __future__ import annotations

import argparse
import os
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent


class DemoServer(ThreadingHTTPServer):
    """A local development server that releases its port immediately."""

    allow_reuse_address = True


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="启动直渠握手本地预览服务")
    parser.add_argument("--host", default="127.0.0.1", help="监听地址")
    parser.add_argument("--port", type=int, default=8000, help="监听端口")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    handler = partial(SimpleHTTPRequestHandler, directory=os.fspath(PROJECT_ROOT))
    with DemoServer((args.host, args.port), handler) as server:
        print(f"Channel Nexus: http://{args.host}:{args.port}")
        print("Press Ctrl+C to stop.")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")


if __name__ == "__main__":
    main()
