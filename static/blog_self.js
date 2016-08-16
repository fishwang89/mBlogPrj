/**
 * Created by 706wangyu on 2016/8/12.
 */
function delHtmlTag(str){
    var src_str = str.replace(/<[^>]+>/g,"")
    return src_str.slice(0, 100);
}
