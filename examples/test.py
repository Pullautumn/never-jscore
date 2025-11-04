import never_jscore as execjs

# 从文件编译
ctx = execjs.compile_file("demo.js")
# result = ctx.call("get_token", ['5fffa6895ac0748d8c76e61c1f4066d73d6501cf63c3221234'])
result = ctx.call("arraytest",[])
print(result)

del ctx
# 从文件执行
result = execjs.eval_file("demo.js")
print(result)

