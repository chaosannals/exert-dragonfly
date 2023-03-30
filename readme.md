# exert dragonfly

## Docker

默认 bind localhost 只能 docker 内连接。
- Docker 内 redis-cli 可以连上。

Windows 下 配置 --bind 0.0.0.0 后：
- telnet 可以连接。
- Python redis 客户端可以连上
- Redis 图形化客户端一开始连不上，时隔 2小时候，Python redis 连上后就可以连接。
