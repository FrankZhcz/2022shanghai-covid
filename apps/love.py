import streamlit as st
import random
from PIL import Image
from content import warmly_moments_list
from utils import chunk_list

def app():
    """
    汇集温暖瞬间
    """

    ##############################################################
    st.write("## 💝汇聚温暖瞬间")
    
    st.info("""
             **人与人之间互传播的还有温暖和感动.**
             
             感谢疫情以来, 每一位奋战在一线的平凡而伟大的工作人员、志愿者们. 你们辛苦了!
             
             疫情阶段很多感动的瞬间, 值得被传递. 让我们多些理解,多方配合,相信疫情很快就会过去.
             
             """)
    st.write(".")
    
    warmly_moments_list.reverse()
    iter_data = chunk_list(warmly_moments_list,10)
    global select_data
    
    select_data = next(iter_data)
    
    
    # def random_sample_list(num=10):
    #     global select_data
    #     select_data = random.sample(warmly_moments_list, num) 
    
    def iterate_warm_moments():
        global select_data
        try:
            select_data = next(iter_data)
        except:
            select_data = []
            
    
    
    st.error(f"**累计收集: {len(warmly_moments_list)} 个暖心瞬间❤️.**")
    expander = st.expander("欢迎投稿-投稿方式>>>")
    expander.write("""
                - [邮箱](kevin_meng@yeah.net)
                - 微信群
                
                .
                """)
    qrcode = Image.open("./files/qrcode.jpeg")
    expander.image(qrcode)
    expander.write("""
                投稿格式:
                - 事情经过(时间\地点\人物\过程...)
                - 配图(可选)
                - 投稿人昵称
                此外, 任何其他有帮助的信息以及内容建议,也可以通过以上两种方式联系我.
                """)
    
    st.write('---')
    st.write("*随机呈现10个瞬间")
    st.button("换一组",key=0,on_click=iterate_warm_moments)
    
    if len(select_data)>0:
        for data in select_data:
            with st.container():
                img = Image.open(data['images'])
                st.image(img)
                # expander = st.expander(data['content'][:50])
                st.warning(data['content'])
            st.write('---')
        st.button("换一组",key=1,on_click=iterate_warm_moments)    
    else:
        st.info("-----已经到底咯-----")
    


