# -*-coding：utf-8-*-
# @Time         :2020/3/6/18:40
# @Author       :Lwf
# @Email        :S
# @File         :test_recommendation.py

third_category = current_test.third_category   # third_category是三级类别的id
test_list = get_tests_by_category(third_category)  #
if len(test_list) < n:
    secondary_category = third_category.get_secondary_category()
    all_third_categories = get_third_category(secondary_category)
    # 随机pick一个third_category
    random_third_category = random.sample(all_third_categories,1)
    other_test_list = get_tests_by_category(random_third_category)
# 从other_test_list中挑选,补齐n个
other_test_list = other_test_list.remove(current_test.third_category)
    other_test_list = random.sample(other_test_list,n-len(test_list))

    #merge two lists,得到结果
    test_list = test_list + other_test_list
else
    random.sample(test_list,n)

r = redis.Redis(host='localhost', port=6379, db=0)

def get_tests_by_category(category):
    # 生成缓存key，这里就用三级分类的id组合一下作为key
    cache_key = "cate" + str(category)
    # 检查redis中是否有缓存
    if r.exists(cache_key):
        return r.get(cache_key)
    else
        # 查询数据库
        test_list =get_from_db(category)
        r.set(cache_key,test_list)
def get_from_db()