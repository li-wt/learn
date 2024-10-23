


# 爬虫
  - 请求
  - 请求头
  - 参数

# 解析
    - re
    - xpath

# 存储
    - mysql
        - DBeaver  可视化工具
    - redis
        - docker run -p 6379:6379 --name redis -v /opt/redis/redis.conf:/etc/redis/redis.conf -v /opt/redis/data:/data -d redis redis-server /etc/redis/redis.conf 
        - docker run -p 本地:容器  --name 名称   -v 本地文件路径:容器文件路径   -d  redis redis-server 配容器文件路径
# 调度
    -redis


    docker run --name my-redis -v D:\redis\redis.conf:/usr/local/etc/redis/redis.conf -p 6379:6379 -d redis redis-server /usr/local/etc/redis/redis.conf


# 仓库地址
https://github.com/li-wt/learn