import streamlit as st
import requests
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import json
import os

st.set_page_config(page_title="EduPredict Pro",page_icon="📊",layout="wide",initial_sidebar_state="expanded")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=DM+Mono:wght@300;400;500&display=swap');
html,body,[class*="css"]{font-family:'Syne',sans-serif!important;background-color:#0a0a0f!important;color:#e8e6f0!important;}
#MainMenu,footer,header{visibility:hidden;}
.stApp{background:#0a0a0f!important;}
[data-testid="stSidebar"]{background:#0d0d18!important;border-right:1px solid #1a1a2e!important;}
[data-testid="stSidebar"] *{color:#e8e6f0!important;}
div[data-testid="stMetricValue"]{color:#ffffff!important;font-family:'Syne',sans-serif!important;font-size:1.8rem!important;font-weight:800!important;}
div[data-testid="stMetricLabel"]{color:#4a4a6a!important;font-family:'DM Mono',monospace!important;font-size:0.65rem!important;text-transform:uppercase!important;letter-spacing:0.1em!important;}
.stButton>button{background:#6c63ff!important;color:white!important;border:none!important;border-radius:8px!important;font-family:'Syne',sans-serif!important;font-weight:700!important;padding:0.6rem 2rem!important;width:100%!important;}
.stButton>button:hover{background:#5a52e0!important;}
label,.stSlider label{color:#a0a0c0!important;font-family:'Syne',sans-serif!important;font-size:0.85rem!important;}
.st{font-family:'DM Mono',monospace;font-size:0.62rem;color:#2a2a4a;text-transform:uppercase;letter-spacing:0.14em;padding-bottom:8px;border-bottom:1px solid #1a1a2e;margin-bottom:14px;}
.role-badge-admin{background:#16163a;color:#6c63ff;border:1px solid #4a3fd4;padding:4px 12px;border-radius:999px;font-size:0.65rem;font-family:'DM Mono',monospace;display:inline-block;}
.role-badge-faculty{background:#0d2b1a;color:#4ade80;border:1px solid #166534;padding:4px 12px;border-radius:999px;font-size:0.65rem;font-family:'DM Mono',monospace;display:inline-block;}
.role-badge-student{background:#2b2200;color:#fbbf24;border:1px solid #92400e;padding:4px 12px;border-radius:999px;font-size:0.65rem;font-family:'DM Mono',monospace;display:inline-block;}
.gb-A{background:#0d2b1a;color:#4ade80;border:1px solid #166534;padding:8px 24px;border-radius:12px;font-size:2.8rem;font-weight:800;display:inline-block;}
.gb-B{background:#0d2020;color:#34d399;border:1px solid #065f46;padding:8px 24px;border-radius:12px;font-size:2.8rem;font-weight:800;display:inline-block;}
.gb-C{background:#2b2200;color:#fbbf24;border:1px solid #92400e;padding:8px 24px;border-radius:12px;font-size:2.8rem;font-weight:800;display:inline-block;}
.gb-D{background:#2b1200;color:#fb923c;border:1px solid #9a3412;padding:8px 24px;border-radius:12px;font-size:2.8rem;font-weight:800;display:inline-block;}
.gb-F{background:#2b0a0a;color:#f87171;border:1px solid #991b1b;padding:8px 24px;border-radius:12px;font-size:2.8rem;font-weight:800;display:inline-block;}
.rl{background:#0d2b1a;color:#4ade80;border:1px solid #166534;padding:4px 14px;border-radius:999px;font-size:0.75rem;font-family:'DM Mono',monospace;display:inline-block;}
.rm{background:#2b2200;color:#fbbf24;border:1px solid #92400e;padding:4px 14px;border-radius:999px;font-size:0.75rem;font-family:'DM Mono',monospace;display:inline-block;}
.rh{background:#2b0a0a;color:#f87171;border:1px solid #991b1b;padding:4px 14px;border-radius:999px;font-size:0.75rem;font-family:'DM Mono',monospace;display:inline-block;}
.rc{background:#12121f;border:1px solid #1a1a2e;border-left:3px solid #6c63ff;border-radius:8px;padding:10px 14px;margin-bottom:8px;font-size:0.8rem;color:#8a8aaa;line-height:1.6;}
.ic{background:#0d0d18;border:1px solid #1a1a2e;border-radius:12px;padding:16px;margin-bottom:10px;}
.ii{font-size:0.78rem;color:#8a8aaa;padding:6px 0;border-bottom:1px solid #0f0f1a;line-height:1.5;}
.ii:last-child{border:none;}
.ah{background:#140808;border:1px solid #7f1d1d;border-left:3px solid #ef4444;border-radius:10px;padding:12px 16px;margin-bottom:10px;}
.am2{background:#14100a;border:1px solid #78350f;border-left:3px solid #f59e0b;border-radius:10px;padding:12px 16px;margin-bottom:10px;}
.anh{color:#f87171;font-weight:700;font-size:0.85rem;margin-bottom:3px;}
.anm{color:#fbbf24;font-weight:700;font-size:0.85rem;margin-bottom:3px;}
.amsg{font-size:0.75rem;color:#4a4a6a;font-family:'DM Mono',monospace;line-height:1.5;}
.pd{background:#0a1a0f;border:1px solid #4ade8040;border-radius:10px;padding:12px;text-align:center;}
.pa{background:#0f0f20;border:1px solid #6c63ff;border-radius:10px;padding:12px;text-align:center;box-shadow:0 0 14px rgba(108,99,255,0.15);}
.pn2{font-size:0.78rem;font-weight:600;color:#e8e6f0;margin:6px 0 3px;}
.pdesc{font-family:'DM Mono',monospace;font-size:0.58rem;color:#2a2a4a;}
.bd{background:#0d2b1a;color:#4ade80;border:1px solid #166534;padding:2px 8px;border-radius:999px;font-size:0.6rem;font-family:'DM Mono',monospace;}
.ba{background:#16163a;color:#6c63ff;border:1px solid #4a3fd4;padding:2px 8px;border-radius:999px;font-size:0.6rem;font-family:'DM Mono',monospace;}
.denied{background:#140808;border:1px solid #7f1d1d;border-radius:12px;padding:2rem;text-align:center;margin-top:2rem;}
.denied-text{color:#f87171;font-size:0.9rem;font-family:'DM Mono',monospace;}
</style>
""", unsafe_allow_html=True)

API   = "http://localhost:8000"
COLORS= {"A":"#4ade80","B":"#34d399","C":"#fbbf24","D":"#fb923c","F":"#f87171"}
GC    = "#1a1a2e"
TC    = "#3a3a5a"
BASE  = os.path.join("C:\\","Users","Dell","student-performance-system")
UPATH = os.path.join(BASE,"users.json")
SPATH = os.path.join(BASE,"students.json")

def pc():
    return dict(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',
                font=dict(family='DM Mono',color='#3a3a5a',size=11),margin=dict(l=0,r=0,t=10,b=0))

def stt(t): return f"<div class='st'>{t}</div>"

def load_users():
    try:
        with open(UPATH,"r") as f: return json.load(f)["users"]
    except: return []

def save_users(u):
    with open(UPATH,"w") as f: json.dump({"users":u},f,indent=2)

def load_students():
    try:
        with open(SPATH,"r") as f: return json.load(f)["students"]
    except: return []

def save_students(s):
    with open(SPATH,"w") as f: json.dump({"students":s},f,indent=2)

def get_student_by_username(uname):
    for s in load_students():
        if s.get("username")==uname: return s
    return None

def authenticate(username,password):
    for u in load_users():
        if u["username"]==username and u["password"]==password: return u
    return None

def is_logged_in(): return "user" in st.session_state and st.session_state.user is not None
def get_role(): return st.session_state.user["role"] if is_logged_in() else None
def can_access(roles): return get_role() in roles

def access_denied():
    st.markdown("<div class='denied'><div style='font-size:2.5rem;margin-bottom:1rem;'>🔒</div><div class='denied-text'>Access Denied — You don't have permission to view this page.</div></div>",unsafe_allow_html=True)

def show_login():
    st.markdown("<div style='display:flex;justify-content:center;margin-top:2rem;'><div style='text-align:center;'><div style='font-size:1.6rem;font-weight:800;color:#fff;'>Edu<span style=\"color:#6c63ff;\">Predict</span> Pro</div><div style='font-family:DM Mono,monospace;font-size:0.6rem;color:#2a2a4a;text-transform:uppercase;letter-spacing:0.15em;margin-bottom:2rem;'>Student Intelligence Platform · Sign In</div></div></div>",unsafe_allow_html=True)
    c1,c2,c3=st.columns([1,1.2,1])
    with c2:
        st.markdown("<div style='background:#0d0d18;border:1px solid #1a1a2e;border-radius:16px;padding:2.5rem;'>",unsafe_allow_html=True)
        st.markdown("<div style='font-size:0.75rem;color:#4a4a6a;font-family:DM Mono,monospace;margin-bottom:1rem;'>Sign in to your account</div>",unsafe_allow_html=True)
        username=st.text_input("Username",placeholder="Enter username")
        password=st.text_input("Password",placeholder="Enter password",type="password")
        st.markdown("<br>",unsafe_allow_html=True)
        if st.button("Sign In →"):
            if username and password:
                u=authenticate(username,password)
                if u:
                    st.session_state.user=u
                    st.success(f"Welcome {u['name']}!")
                    st.rerun()
                else:
                    st.error("Invalid username or password.")
            else:
                st.warning("Please enter both username and password.")
        st.markdown("<hr style='border:none;border-top:1px solid #1a1a2e;margin:1.5rem 0;'>",unsafe_allow_html=True)
        st.markdown("<div style='font-family:DM Mono,monospace;font-size:0.6rem;color:#2a2a4a;'><div style='margin-bottom:6px;'>Demo credentials:</div><div style='margin-bottom:3px;'>Admin &nbsp;→ admin / admin123</div><div style='margin-bottom:3px;'>Faculty → faculty1 / faculty123</div><div>Student → student1 / student123</div></div>",unsafe_allow_html=True)
        st.markdown("</div>",unsafe_allow_html=True)

def show_manage_users():
    st.markdown(stt("Manage Users — Admin Only"),unsafe_allow_html=True)
    users=load_users()
    st.markdown("<div style='font-size:0.82rem;font-weight:600;color:#fff;margin-bottom:12px;'>Current Users</div>",unsafe_allow_html=True)
    for i,u in enumerate(users):
        c1,c2,c3,c4,c5=st.columns([2,2,2,1.5,1])
        c1.markdown(f"<div style='color:#e8e6f0;font-weight:600;font-size:0.8rem;padding:8px 0;'>{u['name']}</div>",unsafe_allow_html=True)
        c2.markdown(f"<div style='color:#4a4a6a;font-family:DM Mono,monospace;font-size:0.72rem;padding:8px 0;'>{u['username']}</div>",unsafe_allow_html=True)
        role_val = u['role']
        c3.markdown(f"<div style='padding:8px 0;'><span class='role-badge-{role_val}'>{role_val.upper()}</span></div>",unsafe_allow_html=True)
        c4.markdown(f"<div style='color:#4a4a6a;font-family:DM Mono,monospace;font-size:0.72rem;padding:8px 0;'>{'•'*len(u['password'])}</div>",unsafe_allow_html=True)
        with c5:
            if u['username']!='admin':
                if st.button("Remove",key=f"rmu{i}"):
                    users.pop(i);save_users(users);st.success("Removed!");st.rerun()
    st.markdown("<hr style='border:none;border-top:1px solid #1a1a2e;margin:1.5rem 0;'>",unsafe_allow_html=True)
    st.markdown("<div style='font-size:0.82rem;font-weight:600;color:#fff;margin-bottom:12px;'>Add New User</div>",unsafe_allow_html=True)
    n1,n2,n3,n4=st.columns(4)
    nm=n1.text_input("Full Name");un=n2.text_input("Username");pw=n3.text_input("Password",type="password");rl=n4.selectbox("Role",["faculty","student"])
    if st.button("Add User →"):
        if nm and un and pw:
            if un in [u["username"] for u in users]: st.error("Username exists!")
            else:
                users.append({"username":un,"password":pw,"role":rl,"name":nm})
                save_users(users);st.success(f"{nm} added!");st.rerun()
        else: st.warning("Fill all fields.")

# ══════════════════════════════════════════════════════
if not is_logged_in():
    show_login()
else:
    user=st.session_state.user
    role=user["role"]

    with st.sidebar:
        st.markdown(f"<div style='margin-bottom:4px;'><span style='font-size:1.3rem;font-weight:800;color:#fff;'>Edu<span style=\"color:#6c63ff;\">Predict</span></span><span style='font-size:0.6rem;color:#2a2a4a;font-family:DM Mono,monospace;margin-left:4px;'>Pro</span></div><div style='font-family:DM Mono,monospace;font-size:0.55rem;color:#2a2a4a;letter-spacing:0.15em;text-transform:uppercase;margin-bottom:1rem;'>Student Intelligence Platform</div><div style='background:#0d0d18;border:1px solid #1a1a2e;border-radius:10px;padding:10px 12px;margin-bottom:1rem;'><div style='font-size:0.78rem;font-weight:600;color:#fff;margin-bottom:3px;'>{user['name']}</div><div><span class='role-badge-{role}'>{role.upper()}</span></div></div>",unsafe_allow_html=True)
        if role in ["admin","faculty"]:
            all_pages=["📊 Dashboard","⚡ Real-time Prediction","🤖 ML Pipeline","🔬 EDA","📈 Visualization","💡 Insights Generator","⚠️ At-Risk Students","🔔 Alerts","📋 Student Records"]
        else:
            all_pages=["👤 My Details","⚡ My Prediction"]
        if role=="admin": all_pages.append("👥 Manage Users")
        page=st.radio("",all_pages,label_visibility="collapsed")
        st.markdown("<hr style='border:none;border-top:1px solid #1a1a2e;margin:1rem 0;'>",unsafe_allow_html=True)
        st.markdown("<div style='font-family:DM Mono,monospace;font-size:0.6rem;'><div style='font-size:0.55rem;color:#2a2a4a;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:8px;'>Model Info</div><div style='display:flex;justify-content:space-between;color:#3a3a5a;margin-bottom:4px;'><span>Algorithm</span><span style='color:#6c63ff;'>Random Forest</span></div><div style='display:flex;justify-content:space-between;color:#3a3a5a;margin-bottom:4px;'><span>Accuracy</span><span style='color:#6c63ff;'>87%</span></div><div style='display:flex;justify-content:space-between;color:#3a3a5a;margin-bottom:4px;'><span>Features</span><span style='color:#6c63ff;'>6 inputs</span></div><div style='display:flex;justify-content:space-between;margin-top:6px;'><span style='color:#3a3a5a;'><span style='color:#4ade80;'>●</span> API</span><span style='color:#4ade80;'>Live</span></div></div>",unsafe_allow_html=True)
        st.markdown("<br>",unsafe_allow_html=True)
        if st.button("🚪 Sign Out"):
            st.session_state.user=None;st.rerun()

    # ══ DASHBOARD ══════════════════════════════════════
    if page=="📊 Dashboard":
        if not can_access(["admin","faculty"]): access_denied()
        else:
            st.markdown(stt("Cohort Overview Dashboard"),unsafe_allow_html=True)
            c1,c2,c3,c4=st.columns(4)
            c1.metric("Total Students","248","enrolled");c2.metric("At Risk","31","12.5% of cohort")
            c3.metric("Avg Predicted Grade","B−","↑ from C+");c4.metric("Avg Attendance","81%","target 85%")
            st.markdown("<br>",unsafe_allow_html=True)
            col1,col2=st.columns(2)
            with col1:
                st.markdown(stt("Grade distribution"),unsafe_allow_html=True)
                f=go.Figure(go.Bar(x=['A','B','C','D','F'],y=[48,82,71,31,16],marker=dict(color=['#4ade80','#34d399','#fbbf24','#fb923c','#f87171'],line=dict(width=0)),text=[48,82,71,31,16],textposition='outside',textfont=dict(color='#4a4a6a',size=11,family='DM Mono')))
                f.update_layout(**pc(),height=260,xaxis=dict(showgrid=False,tickfont=dict(color=TC)),yaxis=dict(gridcolor=GC,tickfont=dict(color=TC)))
                st.plotly_chart(f,use_container_width=True,config={"displayModeBar":False})
            with col2:
                st.markdown(stt("Risk level breakdown"),unsafe_allow_html=True)
                f2=go.Figure(go.Pie(labels=['Low Risk','Medium Risk','High Risk'],values=[169,48,31],marker=dict(colors=['#4ade80','#fbbf24','#f87171'],line=dict(width=0)),hole=0.62,textinfo='none'))
                f2.add_annotation(text="248<br>students",x=0.5,y=0.5,showarrow=False,font=dict(size=14,color='#ffffff',family='Syne'))
                f2.update_layout(**pc(),height=260,legend=dict(font=dict(color=TC,size=11,family='DM Mono'),bgcolor='rgba(0,0,0,0)'))
                st.plotly_chart(f2,use_container_width=True,config={"displayModeBar":False})
            col3,col4=st.columns(2)
            with col3:
                st.markdown(stt("Attendance breakdown (pie)"),unsafe_allow_html=True)
                f3=go.Figure(go.Pie(labels=['Excellent 90-100%','Good 75-89%','Average 60-74%','Poor <60%'],values=[72,98,47,31],marker=dict(colors=['#4ade80','#6c63ff','#fbbf24','#f87171'],line=dict(width=0)),textinfo='none'))
                f3.update_layout(**pc(),height=240,legend=dict(font=dict(color=TC,size=10,family='DM Mono'),bgcolor='rgba(0,0,0,0)'))
                st.plotly_chart(f3,use_container_width=True,config={"displayModeBar":False})
            with col4:
                st.markdown(stt("Performance trend over weeks"),unsafe_allow_html=True)
                wks=['Wk1','Wk2','Wk3','Wk4','Wk5','Wk6','Wk7','Wk8']
                f4=go.Figure()
                f4.add_trace(go.Scatter(x=wks,y=[68,70,69,72,71,74,76,78],name='Class Avg',line=dict(color='#6c63ff',width=2),fill='tozeroy',fillcolor='rgba(108,99,255,0.07)',mode='lines+markers',marker=dict(color='#6c63ff',size=5)))
                f4.add_trace(go.Scatter(x=wks,y=[52,50,49,47,45,44,46,45],name='At-Risk',line=dict(color='#f87171',width=2),fill='tozeroy',fillcolor='rgba(248,113,113,0.05)',mode='lines+markers',marker=dict(color='#f87171',size=5)))
                f4.update_layout(**pc(),height=240,xaxis=dict(gridcolor=GC,tickfont=dict(color=TC)),yaxis=dict(gridcolor=GC,tickfont=dict(color=TC)),legend=dict(font=dict(color=TC,size=10,family='DM Mono'),bgcolor='rgba(0,0,0,0)'))
                st.plotly_chart(f4,use_container_width=True,config={"displayModeBar":False})
            st.markdown(stt("Attendance vs performance (scatter)"),unsafe_allow_html=True)
            np.random.seed(7)
            att=np.random.randint(40,100,80);perf=np.clip(att*0.6+np.random.randint(-15,15,80),30,100)
            f5=go.Figure()
            for lbl,clr,lo,hi in [('Low Risk','#4ade80',70,101),('Medium Risk','#fbbf24',55,70),('High Risk','#f87171',0,55)]:
                idx=[i for i,p in enumerate(perf) if lo<=p<hi]
                f5.add_trace(go.Scatter(x=[att[i] for i in idx],y=[perf[i] for i in idx],mode='markers',name=lbl,marker=dict(color=clr,size=7,opacity=0.8,line=dict(width=0))))
            f5.update_layout(**pc(),height=220,xaxis=dict(title=dict(text='Attendance %',font=dict(color='#2a2a4a')),gridcolor=GC,tickfont=dict(color=TC)),yaxis=dict(title=dict(text='Performance %',font=dict(color='#2a2a4a')),gridcolor=GC,tickfont=dict(color=TC)),legend=dict(font=dict(color=TC,size=10,family='DM Mono'),bgcolor='rgba(0,0,0,0)'))
            st.plotly_chart(f5,use_container_width=True,config={"displayModeBar":False})

    # ══ PREDICTION ══════════════════════════════════════
    elif page in ["⚡ Real-time Prediction","⚡ My Prediction"]:
        if role=="student": st.markdown(stt(f"My Performance Prediction — {user['name']}"),unsafe_allow_html=True)
        else: st.markdown(stt("Real-time Prediction Engine"),unsafe_allow_html=True)
        col1,col2=st.columns([1,1],gap="large")
        with col1:
            st.markdown(stt("Academic inputs"),unsafe_allow_html=True)
            attendance=st.slider("Attendance Rate (%)",0,100,78)
            assignment_avg=st.slider("Assignment Average (%)",0,100,72)
            midterm_score=st.slider("Mid-term Score (%)",0,100,65)
            quiz_avg=st.slider("Quiz Average (%)",0,100,70)
            late_sub=st.slider("Late Submissions",0,15,3)
            study_hours=st.slider("Study Hours / Week",0,40,8)
            predict_btn=st.button("⚡ Run Prediction →")
        with col2:
            if predict_btn:
                with st.spinner("Analyzing..."):
                    try:
                        res=requests.post(f"{API}/predict",json={"attendance":attendance,"assignment_avg":assignment_avg,"midterm_score":midterm_score,"quiz_avg":quiz_avg,"late_submissions":late_sub,"study_hours":study_hours},timeout=5)
                        st.session_state.result=res.json()
                    except: st.error("FastAPI not running! Start: uvicorn api.main:app --reload")
            if "result" in st.session_state:
                r=st.session_state.result
                grade=r.get("predicted_grade","B");risk=r.get("risk_level","Medium");conf=r.get("confidence",70)
                st.markdown(stt("Prediction result"),unsafe_allow_html=True)
                rc1,rc2=st.columns(2)
                with rc1:
                    st.markdown(f"<div class='gb-{grade}'>{grade}</div>",unsafe_allow_html=True)
                    rc={"Low":"rl","Medium":"rm","High":"rh"}.get(risk,"rl")
                    st.markdown(f"<br><div class='{rc}'>{risk} Risk</div>",unsafe_allow_html=True)
                with rc2:
                    st.metric("Confidence",f"{conf}%");st.metric("Predicted Grade",grade)
                st.markdown(stt("Feature importance (XAI)"),unsafe_allow_html=True)
                fi=r.get("feature_importances",{"attendance":0.27,"assignment_avg":0.22,"midterm_score":0.38,"quiz_avg":0.18,"late_submissions":0.14,"study_hours":0.12})
                fi_df=pd.DataFrame(fi.items(),columns=["Feature","Importance"])
                fi_df["Feature"]=fi_df["Feature"].str.replace("_"," ").str.title()
                fi_df=fi_df.sort_values("Importance")
                ff=go.Figure(go.Bar(x=fi_df["Importance"],y=fi_df["Feature"],orientation='h',marker=dict(color=fi_df["Importance"],colorscale=[[0,"#1e1e3a"],[0.5,"#4a3fd4"],[1,"#6c63ff"]],line=dict(width=0))))
                ff.update_layout(**pc(),height=200,xaxis=dict(showgrid=False,zeroline=False,showticklabels=False),yaxis=dict(showgrid=False,zeroline=False,tickfont=dict(color=TC)))
                st.plotly_chart(ff,use_container_width=True,config={"displayModeBar":False})
                st.markdown(stt("Grade probability distribution"),unsafe_allow_html=True)
                gp=r.get("grade_probabilities",{"A":5,"B":25,"C":35,"D":25,"F":10})
                fg=go.Figure(go.Bar(x=list(gp.keys()),y=list(gp.values()),marker=dict(color=[COLORS.get(g,'#6c63ff') for g in gp.keys()],opacity=0.75,line=dict(width=0)),text=[f"{v}%" for v in gp.values()],textposition='outside',textfont=dict(color=TC,size=10,family='DM Mono')))
                fg.update_layout(**pc(),height=180,xaxis=dict(showgrid=False,tickfont=dict(color=TC)),yaxis=dict(gridcolor=GC,tickfont=dict(color=TC)))
                st.plotly_chart(fg,use_container_width=True,config={"displayModeBar":False})
        if "result" in st.session_state:
            r=st.session_state.result
            col3,col4=st.columns(2)
            with col3:
                st.markdown(stt("Skill radar profile"),unsafe_allow_html=True)
                vals=[attendance,assignment_avg,midterm_score,quiz_avg,min(study_hours*2.5,100),max(0,100-late_sub*6.5)]
                cats=['Attendance','Assignments','Midterm','Quizzes','Study Hrs','Submission']
                fr=go.Figure()
                fr.add_trace(go.Scatterpolar(r=vals+[vals[0]],theta=cats+[cats[0]],fill='toself',fillcolor='rgba(108,99,255,0.15)',line=dict(color='#6c63ff',width=2),name='Student',mode='lines+markers',marker=dict(color='#6c63ff',size=5)))
                fr.add_trace(go.Scatterpolar(r=[81,75,72,74,55,74,81],theta=cats+[cats[0]],fill='toself',fillcolor='rgba(74,222,128,0.06)',line=dict(color='#4ade80',width=1.5,dash='dot'),name='Class Avg'))
                fr.update_layout(**pc(),height=280,polar=dict(bgcolor='rgba(0,0,0,0)',angularaxis=dict(tickfont=dict(color=TC,size=10),gridcolor=GC,linecolor=GC),radialaxis=dict(tickfont=dict(color=TC,size=9),gridcolor=GC,linecolor=GC,range=[0,100])),legend=dict(font=dict(color=TC,size=10,family='DM Mono'),bgcolor='rgba(0,0,0,0)'))
                st.plotly_chart(fr,use_container_width=True,config={"displayModeBar":False})
            with col4:
                st.markdown(stt("Subject-wise scores"),unsafe_allow_html=True)
                subj=r.get("subject_scores",{"Mathematics":72,"Science":65,"English":80,"History":58,"Computer Science":88,"Physics":49,"Chemistry":61})
                for sub2,sv in subj.items():
                    sv=min(100,max(0,int(sv)));c2='#4ade80' if sv>=70 else '#fbbf24' if sv>=55 else '#ef4444'
                    st.markdown(f"<div style='margin-bottom:9px;'><div style='display:flex;justify-content:space-between;font-size:0.75rem;color:#4a4a6a;font-family:DM Mono,monospace;margin-bottom:4px;'><span>{sub2}</span><span style='color:#e8e6f0;font-weight:500;'>{sv}%</span></div><div style='height:5px;background:#1a1a2e;border-radius:3px;overflow:hidden;'><div style='width:{sv}%;height:100%;background:{c2};border-radius:3px;'></div></div></div>",unsafe_allow_html=True)
            st.markdown(stt("Personalized recommendations"),unsafe_allow_html=True)
            rcols=st.columns(2)
            for i,tip in enumerate(r.get("recommendations",[])):
                with rcols[i%2]: st.markdown(f"<div class='rc'>→ {tip}</div>",unsafe_allow_html=True)

    # ══ ML PIPELINE ══════════════════════════════════════
    elif page=="🤖 ML Pipeline":
        if not can_access(["admin","faculty"]): access_denied()
        else:
            st.markdown(stt("ML Pipeline — End to End Workflow"),unsafe_allow_html=True)
            stages=[("📥","Data Ingestion","Load CSV","done"),("🧹","Preprocessing","Clean & encode","done"),("⚙️","Feature Eng.","Scale + select","done"),("🤖","Model Training","Random Forest","active"),("📊","Evaluation","Accuracy & F1","done"),("🔍","XAI","Explainability","done"),("🚀","Deployment","FastAPI + UI","done")]
            cols=st.columns(len(stages))
            for i,(icon,name,desc,status) in enumerate(stages):
                with cols[i]:
                    css="pd" if status=="done" else "pa"
                    badge=f"<span class='bd'>✓ Done</span>" if status=="done" else f"<span class='ba'>● Active</span>"
                    st.markdown(f"<div class='{css}'><div style='font-size:1.3rem;'>{icon}</div><div class='pn2'>{name}</div><div class='pdesc'>{desc}</div><div style='margin-top:6px;'>{badge}</div></div>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            p1,p2,p3=st.columns(3)
            with p1:
                st.markdown(stt("Preprocessing steps"),unsafe_allow_html=True)
                for item in ["Handle missing values (median)","Remove duplicate records","Outlier detection — IQR","Label encode target grades","StandardScaler normalization"]:
                    st.markdown(f"<div class='ii'><span style='color:#4ade80;'>✓</span> {item}</div>",unsafe_allow_html=True)
            with p2:
                st.markdown(stt("Feature engineering"),unsafe_allow_html=True)
                for item in ["6 input features selected","Attendance rate (0–100)","Assignment & quiz averages","Late submission penalty","Study hours per week"]:
                    st.markdown(f"<div class='ii'><span style='color:#6c63ff;'>→</span> {item}</div>",unsafe_allow_html=True)
            with p3:
                st.markdown(stt("Model configuration"),unsafe_allow_html=True)
                for item in ["Algorithm: Random Forest","n_estimators: 100 trees","Train/test split: 80/20","Cross-validation: 5-fold","XAI: feature_importances_"]:
                    st.markdown(f"<div class='ii'><span style='color:#fbbf24;'>◎</span> {item}</div>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            mc1,mc2=st.columns(2)
            with mc1:
                st.markdown(stt("Model evaluation metrics"),unsafe_allow_html=True)
                fm=go.Figure(go.Bar(x=['Accuracy','Precision','Recall','F1','AUC-ROC'],y=[87,83,79,81,89],marker=dict(color=['#6c63ff','#4ade80','#fbbf24','#34d399','#2dd4bf'],line=dict(width=0)),text=[87,83,79,81,89],textposition='outside',textfont=dict(color=TC,size=10,family='DM Mono'),width=0.5))
                fm.update_layout(**pc(),height=260,xaxis=dict(showgrid=False,tickfont=dict(color=TC)),yaxis=dict(gridcolor=GC,tickfont=dict(color=TC),range=[60,100]))
                st.plotly_chart(fm,use_container_width=True,config={"displayModeBar":False})
            with mc2:
                st.markdown(stt("Learning curve (train vs test)"),unsafe_allow_html=True)
                trees=[10,20,30,40,50,60,70,80,90,100]
                flc=go.Figure()
                flc.add_trace(go.Scatter(x=trees,y=[72,76,79,81,83,84,85,86,87,87],name='Train',line=dict(color='#6c63ff',width=2),fill='tozeroy',fillcolor='rgba(108,99,255,0.07)',mode='lines+markers',marker=dict(color='#6c63ff',size=5)))
                flc.add_trace(go.Scatter(x=trees,y=[65,69,73,76,78,80,82,84,86,87],name='Test',line=dict(color='#4ade80',width=2),fill='tozeroy',fillcolor='rgba(74,222,128,0.05)',mode='lines+markers',marker=dict(color='#4ade80',size=5)))
                flc.update_layout(**pc(),height=260,xaxis=dict(title=dict(text='n_estimators',font=dict(color='#2a2a4a')),gridcolor=GC,tickfont=dict(color=TC)),yaxis=dict(gridcolor=GC,tickfont=dict(color=TC),range=[60,92]),legend=dict(font=dict(color=TC,size=10,family='DM Mono'),bgcolor='rgba(0,0,0,0)'))
                st.plotly_chart(flc,use_container_width=True,config={"displayModeBar":False})
            st.markdown(stt("Correct vs misclassified predictions"),unsafe_allow_html=True)
            fcm=go.Figure()
            fcm.add_trace(go.Bar(name='Correct',x=['A','B','C','D','F'],y=[44,76,65,27,14],marker=dict(color='rgba(74,222,128,0.4)',line=dict(color='#4ade80',width=1)),width=0.35))
            fcm.add_trace(go.Bar(name='Misclassified',x=['A','B','C','D','F'],y=[4,6,6,4,2],marker=dict(color='rgba(248,113,113,0.4)',line=dict(color='#f87171',width=1)),width=0.35))
            fcm.update_layout(**pc(),height=220,barmode='group',xaxis=dict(showgrid=False,tickfont=dict(color=TC)),yaxis=dict(gridcolor=GC,tickfont=dict(color=TC)),legend=dict(font=dict(color=TC,size=10,family='DM Mono'),bgcolor='rgba(0,0,0,0)'))
            st.plotly_chart(fcm,use_container_width=True,config={"displayModeBar":False})

    # ══ EDA ══════════════════════════════════════
    elif page=="🔬 EDA":
        if not can_access(["admin","faculty"]): access_denied()
        else:
            st.markdown(stt("Exploratory Data Analysis"),unsafe_allow_html=True)
            e1,e2,e3,e4,e5,e6,e7,e8=st.columns(8)
            for col2,lbl,val,sub in [(e1,"Records","500","entries"),(e2,"Features","6","inputs"),(e3,"Missing","0","clean"),(e4,"Classes","5","A-F"),(e5,"Avg Attend","71.4","%"),(e6,"Avg Midterm","65.2","score"),(e7,"Std Dev","14.3","spread"),(e8,"Outliers","12","removed")]:
                col2.metric(lbl,val,sub)
            st.markdown("<br>",unsafe_allow_html=True)
            ea1,ea2=st.columns(2)
            with ea1:
                st.markdown(stt("Attendance distribution (histogram)"),unsafe_allow_html=True)
                fh=go.Figure(go.Bar(x=['40-50','50-60','60-70','70-80','80-90','90-100'],y=[28,45,82,110,118,117],marker=dict(color='#6c63ff',opacity=0.75,line=dict(color='#6c63ff',width=1))))
                fh.update_layout(**pc(),height=230,xaxis=dict(showgrid=False,tickfont=dict(color=TC)),yaxis=dict(gridcolor=GC,tickfont=dict(color=TC)))
                st.plotly_chart(fh,use_container_width=True,config={"displayModeBar":False})
            with ea2:
                st.markdown(stt("Grade class distribution"),unsafe_allow_html=True)
                fgd=go.Figure(go.Bar(x=['A','B','C','D','F'],y=[96,164,142,62,36],marker=dict(color=['rgba(74,222,128,0.4)','rgba(52,211,153,0.4)','rgba(251,191,36,0.4)','rgba(251,146,60,0.4)','rgba(248,113,113,0.4)'],line=dict(color=['#4ade80','#34d399','#fbbf24','#fb923c','#f87171'],width=1))))
                fgd.update_layout(**pc(),height=230,xaxis=dict(showgrid=False,tickfont=dict(color=TC)),yaxis=dict(gridcolor=GC,tickfont=dict(color=TC)))
                st.plotly_chart(fgd,use_container_width=True,config={"displayModeBar":False})
            st.markdown(stt("Feature correlation heatmap"),unsafe_allow_html=True)
            feats=['Attendance','Assignment','Midterm','Quiz Avg','Late Sub','Study Hrs']
            corr=[[1.00,0.72,0.68,0.61,-0.44,0.58],[0.72,1.00,0.74,0.66,-0.38,0.62],[0.68,0.74,1.00,0.71,-0.42,0.65],[0.61,0.66,0.71,1.00,-0.35,0.59],[-0.44,-0.38,-0.42,-0.35,1.00,-0.31],[0.58,0.62,0.65,0.59,-0.31,1.00]]
            fc=go.Figure(go.Heatmap(z=corr,x=feats,y=feats,colorscale=[[0,'#1a0a0a'],[0.5,'#16163a'],[1,'#6c63ff']],text=[[f"{v:.2f}" for v in row] for row in corr],texttemplate="%{text}",textfont=dict(size=11,family='DM Mono'),showscale=True,zmin=-1,zmax=1))
            fc.update_layout(**pc(),height=300,xaxis=dict(tickfont=dict(color=TC)),yaxis=dict(tickfont=dict(color=TC)))
            st.plotly_chart(fc,use_container_width=True,config={"displayModeBar":False})
            eb1,eb2=st.columns(2)
            with eb1:
                st.markdown(stt("Score distribution by grade"),unsafe_allow_html=True)
                fbp=go.Figure(go.Bar(x=['A','B','C','D','F'],y=[88,75,63,52,41],marker=dict(color=['rgba(74,222,128,0.4)','rgba(52,211,153,0.4)','rgba(251,191,36,0.4)','rgba(251,146,60,0.4)','rgba(248,113,113,0.4)'],line=dict(color=['#4ade80','#34d399','#fbbf24','#fb923c','#f87171'],width=1))))
                fbp.update_layout(**pc(),height=220,xaxis=dict(showgrid=False,tickfont=dict(color=TC)),yaxis=dict(gridcolor=GC,tickfont=dict(color=TC)))
                st.plotly_chart(fbp,use_container_width=True,config={"displayModeBar":False})
            with eb2:
                st.markdown(stt("Study hours vs grade (bubble)"),unsafe_allow_html=True)
                fbb=go.Figure()
                for gl,clr,pts in [('A','#4ade80',[(35,88,18),(30,85,15)]),('B','#6c63ff',[(22,74,14),(18,70,11)]),('C','#fbbf24',[(12,62,11),(10,60,9)]),('D/F','#f87171',[(5,48,10),(4,43,8)])]:
                    fbb.add_trace(go.Scatter(x=[p[0] for p in pts],y=[p[1] for p in pts],mode='markers',name=gl,marker=dict(color=clr,size=[p[2] for p in pts],opacity=0.7,line=dict(color=clr,width=1))))
                fbb.update_layout(**pc(),height=220,xaxis=dict(title=dict(text='Study Hrs/Wk',font=dict(color='#2a2a4a')),gridcolor=GC,tickfont=dict(color=TC)),yaxis=dict(title=dict(text='Avg Score %',font=dict(color='#2a2a4a')),gridcolor=GC,tickfont=dict(color=TC)),legend=dict(font=dict(color=TC,size=10,family='DM Mono'),bgcolor='rgba(0,0,0,0)'))
                st.plotly_chart(fbb,use_container_width=True,config={"displayModeBar":False})

    # ══ VISUALIZATION ══════════════════════════════════════
    elif page=="📈 Visualization":
        if not can_access(["admin","faculty"]): access_denied()
        else:
            st.markdown(stt("Visualization Gallery"),unsafe_allow_html=True)
            v1,v2,v3,v4=st.columns(4)
            v1.metric("Total Charts","18","generated");v2.metric("Data Points","500","records");v3.metric("Dimensions","6×6","heatmap");v4.metric("Weeks Tracked","8","trend data")
            st.markdown("<br>",unsafe_allow_html=True)
            vc1,vc2,vc3=st.columns(3)
            with vc1:
                st.markdown(stt("Line — top vs bottom 25%"),unsafe_allow_html=True)
                wks=['Wk1','Wk2','Wk3','Wk4','Wk5','Wk6','Wk7','Wk8']
                fvl=go.Figure()
                fvl.add_trace(go.Scatter(x=wks,y=[82,84,85,86,87,88,89,90],name='Top 25%',line=dict(color='#4ade80',width=2),mode='lines+markers',marker=dict(size=4)))
                fvl.add_trace(go.Scatter(x=wks,y=[55,53,50,48,46,44,45,44],name='Bottom 25%',line=dict(color='#f87171',width=2),mode='lines+markers',marker=dict(size=4)))
                fvl.update_layout(**pc(),height=200,xaxis=dict(gridcolor=GC,tickfont=dict(color=TC,size=9)),yaxis=dict(gridcolor=GC,tickfont=dict(color=TC,size=9)),legend=dict(font=dict(color=TC,size=9,family='DM Mono'),bgcolor='rgba(0,0,0,0)'))
                st.plotly_chart(fvl,use_container_width=True,config={"displayModeBar":False})
            with vc2:
                st.markdown(stt("Pie — attendance split"),unsafe_allow_html=True)
                fvp=go.Figure(go.Pie(labels=['Excellent','Good','Average','Poor'],values=[72,98,47,31],marker=dict(colors=['#4ade80','#6c63ff','#fbbf24','#f87171'],line=dict(width=0)),textinfo='none'))
                fvp.update_layout(**pc(),height=200,legend=dict(font=dict(color=TC,size=9,family='DM Mono'),bgcolor='rgba(0,0,0,0)'))
                st.plotly_chart(fvp,use_container_width=True,config={"displayModeBar":False})
            with vc3:
                st.markdown(stt("Radar — grade profiles"),unsafe_allow_html=True)
                cats2=['Attend','Assign','Midterm','Quiz','Study','Submit']
                fvr=go.Figure()
                for lbl,vals2,clr in [('Grade A',[92,90,88,87,35,90],'#4ade80'),('Grade C',[72,68,62,66,20,65],'#fbbf24'),('Grade F',[48,44,40,46,8,38],'#f87171')]:
                    fvr.add_trace(go.Scatterpolar(r=vals2+[vals2[0]],theta=cats2+[cats2[0]],fill='toself',name=lbl,line=dict(color=clr,width=1.5),fillcolor='rgba(0,0,0,0.1)'))
                fvr.update_layout(**pc(),height=200,polar=dict(bgcolor='rgba(0,0,0,0)',angularaxis=dict(tickfont=dict(color=TC,size=8),gridcolor=GC,linecolor=GC),radialaxis=dict(tickfont=dict(color=TC,size=7),gridcolor=GC,linecolor=GC,range=[0,100])),legend=dict(font=dict(color=TC,size=9,family='DM Mono'),bgcolor='rgba(0,0,0,0)'))
                st.plotly_chart(fvr,use_container_width=True,config={"displayModeBar":False})
            vc4,vc5=st.columns(2)
            with vc4:
                st.markdown(stt("Grouped bar — scores by risk"),unsafe_allow_html=True)
                fvg=go.Figure()
                for lbl,vals3,clr in [('Low Risk',[88,84,82,80,28],'#4ade80'),('Medium Risk',[71,67,62,66,18],'#fbbf24'),('High Risk',[58,50,47,52,10],'#f87171')]:
                    fvg.add_trace(go.Bar(name=lbl,x=['Attendance','Assignment','Midterm','Quiz','Study Hrs'],y=vals3,marker=dict(color=clr,opacity=0.6,line=dict(color=clr,width=1))))
                fvg.update_layout(**pc(),height=230,barmode='group',xaxis=dict(showgrid=False,tickfont=dict(color=TC,size=9)),yaxis=dict(gridcolor=GC,tickfont=dict(color=TC)),legend=dict(font=dict(color=TC,size=9,family='DM Mono'),bgcolor='rgba(0,0,0,0)'))
                st.plotly_chart(fvg,use_container_width=True,config={"displayModeBar":False})
            with vc5:
                st.markdown(stt("Stacked bar — grade by attendance"),unsafe_allow_html=True)
                fvs=go.Figure()
                for lbl,vals4,clr in [('Grade A',[40,30,15,5],'#4ade80'),('Grade B',[25,45,30,10],'#6c63ff'),('Grade C',[5,15,30,20],'#fbbf24'),('Grade D/F',[2,5,15,30],'#f87171')]:
                    fvs.add_trace(go.Bar(name=lbl,x=['Excellent','Good','Average','Poor'],y=vals4,marker=dict(color=clr,opacity=0.7)))
                fvs.update_layout(**pc(),height=230,barmode='stack',xaxis=dict(showgrid=False,tickfont=dict(color=TC,size=9)),yaxis=dict(gridcolor=GC,tickfont=dict(color=TC)),legend=dict(font=dict(color=TC,size=9,family='DM Mono'),bgcolor='rgba(0,0,0,0)'))
                st.plotly_chart(fvs,use_container_width=True,config={"displayModeBar":False})

    # ══ INSIGHTS ══════════════════════════════════════
    elif page=="💡 Insights Generator":
        if not can_access(["admin","faculty"]): access_denied()
        else:
            st.markdown(stt("AI Insights Generator"),unsafe_allow_html=True)
            i1,i2,i3=st.columns(3)
            i1.metric("Insights Generated","24","this session");i2.metric("Patterns Detected","8","across cohort");i3.metric("Action Alerts","5","need intervention")
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown(stt("AI-generated cohort analysis report"),unsafe_allow_html=True)
            st.markdown("<div style='background:#0a0a14;border:1px solid #1a1a2e;border-radius:10px;padding:16px;font-family:DM Mono,monospace;font-size:0.73rem;color:#6a6a8a;line-height:1.9;margin-bottom:16px;'><span style='color:#6c63ff;font-weight:600;'>COHORT SUMMARY — Spring Term 2025</span><br>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━<br><br>Model analyzed <span style='color:#e8e6f0;'>248 student records</span> and identified <span style='color:#f87171;'>31 students (12.5%)</span> as high or medium risk.<br><br><span style='color:#4ade80;'>KEY FINDINGS:</span><br>• Attendance below 75% — students are <span style='color:#f87171;'>3.2x more likely</span> to receive D or F.<br>• Mid-term scores account for <span style='color:#6c63ff;'>38% of predictive weight</span>.<br>• Each late submission reduces grade by approx <span style='color:#fbbf24;'>4%</span>.<br>• Students studying less than 10 hrs/week are <span style='color:#f87171;'>2.8x more likely</span> to be high risk.<br><br><span style='color:#4ade80;'>RECOMMENDED ACTIONS:</span><br>→ Immediate intervention for Priya K., Kiran R., Arjun M.<br>→ Weekly check-ins for Sara T., Rahul S., Divya P.<br>→ Attendance awareness campaign — 19% below 75% threshold</div>",unsafe_allow_html=True)
            ic1,ic2=st.columns(2)
            insights=[("📈","Performance Insights","grade & score patterns",[("🟢","Top 25% students average 91% attendance"),("🟡","Grade C students show highest improvement potential"),("🔴","Physics and History lowest — 52% and 55%"),("🟣","Computer Science highest at avg 78%")]),("⚠️","Risk Patterns","early warning signals",[("🔴","3+ missed assignments → 89% probability of failing"),("🔴","Attendance drop below 60% in Week 3 is earliest signal"),("🟡","Late submissions >5 correlates with risk in 91% of cases"),("🟡","Quiz decline over 3 weeks is reliable early warning")]),("💡","Study Recommendations","personalized tips",[("01","Add 6+ study hrs/week for one grade improvement"),("02","Focus on weakest subject first"),("03","Peer study groups improve Physics by avg 12%"),("04","Remove late submissions to gain half a letter grade")]),("🎯","Educator Actions","intervention priorities",[("🔴","Priority 1 — Contact Priya K. immediately"),("🔴","Priority 2 — Kiran R. and Arjun M. need support"),("🟡","Priority 3 — Group session for medium-risk students"),("🟣","Run attendance awareness campaign")])]
            for idx,(icon,title,sub,items) in enumerate(insights):
                with (ic1 if idx%2==0 else ic2):
                    st.markdown(f"<div class='ic'><div style='display:flex;align-items:center;gap:8px;margin-bottom:10px;'><span style='font-size:1.1rem;'>{icon}</span><div><div style='font-size:0.82rem;font-weight:600;color:#fff;'>{title}</div><div style='font-family:DM Mono,monospace;font-size:0.55rem;color:#2a2a4a;'>{sub}</div></div></div>",unsafe_allow_html=True)
                    for bullet,text in items:
                        st.markdown(f"<div class='ii'><span style='margin-right:6px;'>{bullet}</span>{text}</div>",unsafe_allow_html=True)
                    st.markdown("</div>",unsafe_allow_html=True)
            ic3,ic4=st.columns(2)
            with ic3:
                st.markdown(stt("Insight categories"),unsafe_allow_html=True)
                fip=go.Figure(go.Pie(labels=['Performance','Risk Patterns','Study Tips','Educator Actions'],values=[30,28,22,20],marker=dict(colors=['#6c63ff','#f87171','#4ade80','#fbbf24'],line=dict(width=0)),textinfo='none'))
                fip.update_layout(**pc(),height=220,legend=dict(font=dict(color=TC,size=10,family='DM Mono'),bgcolor='rgba(0,0,0,0)'))
                st.plotly_chart(fip,use_container_width=True,config={"displayModeBar":False})
            with ic4:
                st.markdown(stt("Intervention impact forecast"),unsafe_allow_html=True)
                fib=go.Figure(go.Bar(x=['Attendance\nCampaign','Study Groups','1-on-1\nCheck-ins','Assignment\nReminders','Peer Tutoring'],y=[0.8,0.6,0.9,0.5,0.7],marker=dict(color=['#6c63ff','#4ade80','#f87171','#fbbf24','#2dd4bf'],opacity=0.75,line=dict(width=0)),text=[0.8,0.6,0.9,0.5,0.7],textposition='outside',textfont=dict(color=TC,size=10,family='DM Mono')))
                fib.update_layout(**pc(),height=220,xaxis=dict(showgrid=False,tickfont=dict(color=TC,size=9)),yaxis=dict(gridcolor=GC,tickfont=dict(color=TC),title=dict(text='Grade Points',font=dict(color='#2a2a4a',size=10))))
                st.plotly_chart(fib,use_container_width=True,config={"displayModeBar":False})

    # ══ AT-RISK ══════════════════════════════════════
    elif page=="⚠️ At-Risk Students":
        if not can_access(["admin","faculty"]): access_denied()
        else:
            st.markdown(stt("At-Risk Students — Early Intervention Required"),unsafe_allow_html=True)
            ss=[{"Name":"Priya K.","Attendance":"55%","Assign":"48%","Midterm":"44%","Risk":"High","Grade":"D","Conf":"82%","Trend":"↓ −12%"},{"Name":"Kiran R.","Attendance":"60%","Assign":"50%","Midterm":"47%","Risk":"High","Grade":"D","Conf":"80%","Trend":"↓ −9%"},{"Name":"Arjun M.","Attendance":"62%","Assign":"55%","Midterm":"51%","Risk":"High","Grade":"D","Conf":"76%","Trend":"↓ −7%"},{"Name":"Sara T.","Attendance":"70%","Assign":"61%","Midterm":"58%","Risk":"Medium","Grade":"C−","Conf":"71%","Trend":"↓ −4%"},{"Name":"Rahul S.","Attendance":"68%","Assign":"63%","Midterm":"60%","Risk":"Medium","Grade":"C","Conf":"68%","Trend":"↑ +2%"},{"Name":"Divya P.","Attendance":"74%","Assign":"66%","Midterm":"59%","Risk":"Medium","Grade":"C","Conf":"73%","Trend":"↑ +1%"}]
            rows=""
            for s in ss:
                rb="#2b0a0a" if s["Risk"]=="High" else "#2b2200";rc2="#f87171" if s["Risk"]=="High" else "#fbbf24";rd="#7f1d1d" if s["Risk"]=="High" else "#78350f";tc2="#f87171" if "↓" in s["Trend"] else "#4ade80"
                rows+=f"<tr><td style='color:#e8e6f0;font-weight:600;'>{s['Name']}</td><td>{s['Attendance']}</td><td>{s['Assign']}</td><td>{s['Midterm']}</td><td><span style='background:{rb};color:{rc2};border:1px solid {rd};padding:2px 9px;border-radius:999px;font-size:0.62rem;font-family:DM Mono,monospace;'>{s['Risk']}</span></td><td style='color:#fff;font-weight:700;'>{s['Grade']}</td><td style='color:#6c63ff;font-family:DM Mono,monospace;'>{s['Conf']}</td><td style='color:{tc2};font-family:DM Mono,monospace;font-size:0.68rem;'>{s['Trend']}</td></tr>"
            headers=['Student','Attendance','Assign Avg','Midterm','Risk','Predicted','Confidence','Trend']
            th="".join(f"<th style='text-align:left;color:#2a2a4a;font-family:DM Mono,monospace;font-size:0.55rem;text-transform:uppercase;letter-spacing:0.1em;padding:7px 9px;border-bottom:1px solid #1a1a2e;font-weight:400;'>{h}</th>" for h in headers)
            st.markdown(f"<div style='background:#0d0d18;border:1px solid #1a1a2e;border-radius:13px;padding:1.1rem;margin-bottom:14px;'><table style='width:100%;border-collapse:collapse;font-size:0.74rem;'><thead><tr>{th}</tr></thead><tbody>{rows}</tbody></table></div>",unsafe_allow_html=True)
            ar1,ar2,ar3=st.columns(3)
            with ar1:
                st.markdown(stt("Performance trend — Priya K."),unsafe_allow_html=True)
                fat=go.Figure(go.Scatter(x=['Wk1','Wk2','Wk3','Wk4','Wk5','Wk6','Wk7','Wk8'],y=[62,60,57,53,50,47,45,44],line=dict(color='#f87171',width=2),fill='tozeroy',fillcolor='rgba(248,113,113,0.07)',mode='lines+markers',marker=dict(color='#f87171',size=5)))
                fat.update_layout(**pc(),height=200,xaxis=dict(gridcolor=GC,tickfont=dict(color=TC,size=9)),yaxis=dict(gridcolor=GC,tickfont=dict(color=TC),range=[30,80]))
                st.plotly_chart(fat,use_container_width=True,config={"displayModeBar":False})
            with ar2:
                st.markdown(stt("Attendance pie — Priya K."),unsafe_allow_html=True)
                fap=go.Figure(go.Pie(labels=['Present','Absent','Late'],values=[55,30,15],marker=dict(colors=['#6c63ff','#f87171','#fbbf24'],line=dict(width=0)),textinfo='none'))
                fap.update_layout(**pc(),height=200,legend=dict(font=dict(color=TC,size=10,family='DM Mono'),bgcolor='rgba(0,0,0,0)'))
                st.plotly_chart(fap,use_container_width=True,config={"displayModeBar":False})
            with ar3:
                st.markdown(stt("Skill radar — Priya K. vs class"),unsafe_allow_html=True)
                cats3=['Attend','Assign','Midterm','Quiz','Study','Submit']
                far=go.Figure()
                far.add_trace(go.Scatterpolar(r=[55,48,44,50,30,40,55],theta=cats3+[cats3[0]],fill='toself',name='Priya K.',line=dict(color='#f87171',width=2),fillcolor='rgba(248,113,113,0.12)'))
                far.add_trace(go.Scatterpolar(r=[81,75,72,74,55,74,81],theta=cats3+[cats3[0]],fill='toself',name='Class Avg',line=dict(color='#4a4a6a',width=1,dash='dot'),fillcolor='rgba(74,74,106,0.05)'))
                far.update_layout(**pc(),height=200,polar=dict(bgcolor='rgba(0,0,0,0)',angularaxis=dict(tickfont=dict(color=TC,size=8),gridcolor=GC,linecolor=GC),radialaxis=dict(tickfont=dict(color=TC,size=7),gridcolor=GC,linecolor=GC,range=[0,100])),legend=dict(font=dict(color=TC,size=9,family='DM Mono'),bgcolor='rgba(0,0,0,0)'))
                st.plotly_chart(far,use_container_width=True,config={"displayModeBar":False})

    # ══ ALERTS ══════════════════════════════════════
    elif page=="🔔 Alerts":
        if not can_access(["admin","faculty"]): access_denied()
        else:
            st.markdown(stt("Educator Alerts — Real-time Monitoring"),unsafe_allow_html=True)
            al1,al2=st.columns(2)
            with al1:
                st.markdown(stt("Weekly at-risk count trend"),unsafe_allow_html=True)
                falt=go.Figure()
                falt.add_trace(go.Scatter(x=['Wk1','Wk2','Wk3','Wk4','Wk5','Wk6','Wk7','Wk8'],y=[18,20,22,25,28,30,31,31],name='High Risk',line=dict(color='#f87171',width=2),fill='tozeroy',fillcolor='rgba(248,113,113,0.07)',mode='lines+markers',marker=dict(color='#f87171',size=5)))
                falt.add_trace(go.Scatter(x=['Wk1','Wk2','Wk3','Wk4','Wk5','Wk6','Wk7','Wk8'],y=[30,32,35,40,44,46,48,48],name='Medium Risk',line=dict(color='#fbbf24',width=2),fill='tozeroy',fillcolor='rgba(251,191,36,0.05)',mode='lines+markers',marker=dict(color='#fbbf24',size=5)))
                falt.update_layout(**pc(),height=230,xaxis=dict(gridcolor=GC,tickfont=dict(color=TC)),yaxis=dict(gridcolor=GC,tickfont=dict(color=TC)),legend=dict(font=dict(color=TC,size=10,family='DM Mono'),bgcolor='rgba(0,0,0,0)'))
                st.plotly_chart(falt,use_container_width=True,config={"displayModeBar":False})
            with al2:
                st.markdown(stt("Alert type distribution"),unsafe_allow_html=True)
                falp=go.Figure(go.Pie(labels=['Low Attendance','Poor Grades','Late Submissions','Low Study Hrs','Exam Risk'],values=[31,24,18,15,12],marker=dict(colors=['#f87171','#fb923c','#fbbf24','#6c63ff','#ef4444'],line=dict(width=0)),textinfo='none'))
                falp.update_layout(**pc(),height=230,legend=dict(font=dict(color=TC,size=10,family='DM Mono'),bgcolor='rgba(0,0,0,0)'))
                st.plotly_chart(falp,use_container_width=True,config={"displayModeBar":False})
            for level,name,msg in [("high","⚠ Priya K. — Immediate Action Required","Attendance 55% · missing 3 assignments · all indicators critical."),("high","⚠ Kiran R. — High Risk Detected","Mid-term 47% · bottom 10% of cohort · recommend counselling now."),("high","⚠ Arjun M. — Consistent Decline","Quiz declining 4 consecutive weeks · at risk of failing."),("med","◎ Sara T. — Monitor Closely","Late submissions increasing · study engagement below average."),("med","◎ Rahul S. — Early Warning","Quiz average declining · recommend 1-on-1 advisor session.")]:
                css="ah" if level=="high" else "am2";ncss="anh" if level=="high" else "anm"
                st.markdown(f"<div class='{css}'><div class='{ncss}'>{name}</div><div class='amsg'>{msg}</div></div>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            am1,am2,am3,am4=st.columns(4)
            am1.metric("Accuracy","87%","model");am2.metric("Precision","83%","score");am3.metric("Recall","79%","score");am4.metric("F1 Score","81%","score")

    # ══ STUDENT RECORDS ══════════════════════════════════════
    elif page=="📋 Student Records":
        if not can_access(["admin","faculty"]): access_denied()
        else:
            st.markdown(stt("Student Records — Manage Academic Data"),unsafe_allow_html=True)
            tab1,tab2,tab3=st.tabs(["📋 View All Students","➕ Add Student","📤 Upload CSV"])
            with tab1:
                students=load_students()
                if not students:
                    st.info("No students added yet. Use Add Student or Upload CSV tab.")
                else:
                    st.markdown(f"<div style='font-family:DM Mono,monospace;font-size:0.7rem;color:#4a4a6a;margin-bottom:1rem;'>Total records: {len(students)}</div>",unsafe_allow_html=True)
                    for i,s in enumerate(students):
                        with st.expander(f"📌 {s['name']} — {s['roll']} | Risk: {s.get('risk_level','Not predicted yet')}"):
                            ec1,ec2,ec3=st.columns(3)
                            with ec1:
                                st.markdown(f"<div style='font-family:DM Mono,monospace;font-size:0.72rem;color:#4a4a6a;'>Roll No</div><div style='color:#fff;font-weight:600;'>{s['roll']}</div>",unsafe_allow_html=True)
                                st.markdown(f"<div style='font-family:DM Mono,monospace;font-size:0.72rem;color:#4a4a6a;margin-top:8px;'>Username</div><div style='color:#6c63ff;font-family:DM Mono,monospace;'>{s.get('username','—')}</div>",unsafe_allow_html=True)
                            with ec2:
                                st.markdown("<div style='font-family:DM Mono,monospace;font-size:0.65rem;color:#2a2a4a;text-transform:uppercase;margin-bottom:6px;'>Academic Data</div>",unsafe_allow_html=True)
                                for label,key in [("Attendance","attendance"),("Assignment Avg","assignment_avg"),("Midterm Score","midterm_score"),("Quiz Avg","quiz_avg")]:
                                    val=s.get(key,0);color='#4ade80' if val>=70 else '#fbbf24' if val>=55 else '#f87171'
                                    st.markdown(f"<div style='display:flex;justify-content:space-between;font-size:0.72rem;margin-bottom:4px;'><span style='color:#4a4a6a;'>{label}</span><span style='color:{color};font-weight:600;'>{val}%</span></div>",unsafe_allow_html=True)
                            with ec3:
                                st.markdown("<div style='font-family:DM Mono,monospace;font-size:0.65rem;color:#2a2a4a;text-transform:uppercase;margin-bottom:6px;'>More Data</div>",unsafe_allow_html=True)
                                for label,key,suffix in [("Late Submissions","late_submissions",""),("Study Hours","study_hours"," hrs/wk")]:
                                    st.markdown(f"<div style='display:flex;justify-content:space-between;font-size:0.72rem;margin-bottom:4px;'><span style='color:#4a4a6a;'>{label}</span><span style='color:#e8e6f0;font-weight:600;'>{s.get(key,0)}{suffix}</span></div>",unsafe_allow_html=True)
                                if s.get('predicted_grade'):
                                    g=s['predicted_grade'];gc=COLORS.get(g,'#6c63ff')
                                    st.markdown(f"<div style='margin-top:8px;'><span style='color:#4a4a6a;font-size:0.72rem;'>Predicted Grade </span><span style='color:{gc};font-size:1.2rem;font-weight:800;'>{g}</span></div>",unsafe_allow_html=True)
                            bc1,bc2,bc3=st.columns(3)
                            with bc1:
                                if st.button("✏️ Edit",key=f"ed{i}"):
                                    st.session_state.edit_student=i;st.session_state.edit_mode=True
                            with bc2:
                                if st.button("⚡ Predict",key=f"pr{i}"):
                                    try:
                                        res=requests.post(f"{API}/predict",json={"attendance":s["attendance"],"assignment_avg":s["assignment_avg"],"midterm_score":s["midterm_score"],"quiz_avg":s["quiz_avg"],"late_submissions":s["late_submissions"],"study_hours":s["study_hours"]},timeout=5)
                                        result=res.json()
                                        students[i]["predicted_grade"]=result["predicted_grade"];students[i]["risk_level"]=result["risk_level"];students[i]["confidence"]=result["confidence"]
                                        save_students(students);st.success(f"Grade {result['predicted_grade']} — {result['risk_level']} Risk ({result['confidence']}%)");st.rerun()
                                    except: st.error("API not running!")
                            with bc3:
                                if st.button("🗑️ Delete",key=f"dl{i}"):
                                    students.pop(i);save_students(students);st.success("Deleted!");st.rerun()
                            if st.session_state.get("edit_mode") and st.session_state.get("edit_student")==i:
                                st.markdown("<hr style='border:none;border-top:1px solid #1a1a2e;margin:1rem 0;'>",unsafe_allow_html=True)
                                st.markdown("<div style='font-size:0.78rem;font-weight:600;color:#6c63ff;margin-bottom:12px;'>Edit Student Data</div>",unsafe_allow_html=True)
                                fc1,fc2=st.columns(2)
                                with fc1:
                                    na=st.slider("Attendance (%)",0,100,int(s["attendance"]),key=f"a{i}")
                                    nb=st.slider("Assignment Avg (%)",0,100,int(s["assignment_avg"]),key=f"b{i}")
                                    nc2=st.slider("Midterm Score (%)",0,100,int(s["midterm_score"]),key=f"c{i}")
                                    nd=st.slider("Quiz Avg (%)",0,100,int(s["quiz_avg"]),key=f"d{i}")
                                with fc2:
                                    ne=st.slider("Late Submissions",0,15,int(s["late_submissions"]),key=f"e{i}")
                                    nf=st.slider("Study Hours/Week",0,40,int(s["study_hours"]),key=f"f{i}")
                                    nu=st.text_input("Username",value=s.get("username",""),key=f"u{i}")
                                if st.button("💾 Save Changes",key=f"sv{i}"):
                                    students[i].update({"attendance":na,"assignment_avg":nb,"midterm_score":nc2,"quiz_avg":nd,"late_submissions":ne,"study_hours":nf,"username":nu})
                                    save_students(students);st.session_state.edit_mode=False;st.success("Updated!");st.rerun()
            with tab2:
                st.markdown("<div style='font-size:0.82rem;font-weight:600;color:#fff;margin-bottom:1rem;'>Add New Student</div>",unsafe_allow_html=True)
                ac1,ac2=st.columns(2)
                with ac1:
                    new_roll=st.text_input("Roll Number",placeholder="e.g. ST007")
                    new_name=st.text_input("Student Name",placeholder="e.g. John D.")
                    new_uname=st.text_input("Username (for login)",placeholder="e.g. student7")
                    new_pass=st.text_input("Password (for login)",placeholder="e.g. pass007",type="password")
                with ac2:
                    na=st.slider("Attendance (%)",0,100,75,key="nadd")
                    nb=st.slider("Assignment Avg (%)",0,100,70,key="nbadd")
                    nc2=st.slider("Midterm Score (%)",0,100,65,key="ncadd")
                    nd=st.slider("Quiz Avg (%)",0,100,70,key="ndadd")
                    ne=st.slider("Late Submissions",0,15,2,key="neadd")
                    nf=st.slider("Study Hours/Week",0,40,10,key="nfadd")
                if st.button("➕ Add Student →"):
                    if new_roll and new_name and new_uname and new_pass:
                        students=load_students()
                        if new_roll in [s["roll"] for s in students]: st.error("Roll number already exists!")
                        else:
                            students.append({"roll":new_roll,"name":new_name,"username":new_uname,"attendance":na,"assignment_avg":nb,"midterm_score":nc2,"quiz_avg":nd,"late_submissions":ne,"study_hours":nf,"predicted_grade":"","risk_level":"","confidence":0})
                            save_students(students)
                            users=load_users()
                            if new_uname not in [u["username"] for u in users]:
                                users.append({"username":new_uname,"password":new_pass,"role":"student","name":new_name});save_users(users)
                            st.success(f"Student {new_name} added with login access!");st.rerun()
                    else: st.warning("Please fill all fields!")
            with tab3:
                st.markdown("<div style='font-size:0.82rem;font-weight:600;color:#fff;margin-bottom:8px;'>Upload Student CSV File</div>",unsafe_allow_html=True)
                st.markdown("<div style='font-family:DM Mono,monospace;font-size:0.65rem;color:#4a4a6a;margin-bottom:1rem;'>Your CSV format is accepted automatically.</div>",unsafe_allow_html=True)
                uploaded=st.file_uploader("Choose CSV file",type=["csv"],key="csvupload")
                if uploaded is not None:
                    try:
                        df=pd.read_csv(uploaded,encoding='latin1')
                        df.columns=df.columns.str.strip()
                        col_map={'Roll Number':'roll','Student Name':'name','Username(for login)':'username','Password(for login)':'password','Attendance(%)':'attendance','Assignment Avg(%)':'assignment_avg','Midterm Score(%)':'midterm_score','Quiz Avg(%)':'quiz_avg','Late Submissions':'late_submissions','Study Hours/Week':'study_hours','roll':'roll','name':'name','username':'username','password':'password','attendance':'attendance','assignment_avg':'assignment_avg','midterm_score':'midterm_score','quiz_avg':'quiz_avg','late_submissions':'late_submissions','study_hours':'study_hours'}
                        df=df.rename(columns={c:col_map[c] for c in df.columns if c in col_map})
                        st.markdown("<div style='font-size:0.75rem;color:#4ade80;margin-bottom:8px;'>File loaded — Preview:</div>",unsafe_allow_html=True)
                        st.dataframe(df.head(5))
                        required=['roll','name','username','attendance','assignment_avg','midterm_score','quiz_avg','late_submissions','study_hours']
                        missing=[c for c in required if c not in df.columns]
                        if missing:
                            st.error(f"Missing columns: {', '.join(missing)}")
                        else:
                            st.success(f"{len(df)} students ready to import!")
                            if st.button("Import All Students",key="importbtn"):
                                students=load_students();existing=[s["roll"] for s in students]
                                users=load_users();existing_u=[u["username"] for u in users]
                                added=0;skipped=0
                                for _,row in df.iterrows():
                                    roll=str(row["roll"]).strip();uname=str(row["username"]).strip()
                                    pwd=str(row["password"]).strip() if "password" in df.columns else uname+"123"
                                    sname=str(row["name"]).strip()
                                    if roll not in existing:
                                        students.append({"roll":roll,"name":sname,"username":uname,"attendance":float(row["attendance"]),"assignment_avg":float(row["assignment_avg"]),"midterm_score":float(row["midterm_score"]),"quiz_avg":float(row["quiz_avg"]),"late_submissions":float(row["late_submissions"]),"study_hours":float(row["study_hours"]),"predicted_grade":"","risk_level":"","confidence":0})
                                        if uname not in existing_u:
                                            users.append({"username":uname,"password":pwd,"role":"student","name":sname});existing_u.append(uname)
                                        added+=1
                                    else:
                                        skipped+=1
                                save_students(students);save_users(users)
                                st.success(f"{added} students imported! {skipped} skipped.")
                                st.info("Students can login with their username and password from the CSV.")
                                st.rerun()
                    except Exception as e:
                        st.error(f"Error reading file: {e}")

    # ══ MY DETAILS (Student) ══════════════════════════════════════
    elif page=="👤 My Details":
        st.markdown(stt(f"My Academic Details — {user['name']}"),unsafe_allow_html=True)
        student=get_student_by_username(user["username"])
        if not student:
            st.markdown("<div style='background:#0d0d18;border:1px solid #1a1a2e;border-radius:12px;padding:2rem;text-align:center;margin-top:1rem;'><div style='font-size:2rem;margin-bottom:1rem;'>📋</div><div style='font-family:DM Mono,monospace;font-size:0.75rem;color:#4a4a6a;'>Your details have not been added yet.<br>Please contact your faculty.</div></div>",unsafe_allow_html=True)
        else:
            dc1,dc2,dc3=st.columns(3)
            with dc1:
                st.markdown(f"<div style='background:#0d0d18;border:1px solid #1a1a2e;border-radius:12px;padding:1.2rem;'><div style='font-family:DM Mono,monospace;font-size:0.55rem;color:#2a2a4a;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:8px;'>Student Info</div><div style='font-size:1rem;font-weight:700;color:#fff;margin-bottom:4px;'>{student['name']}</div><div style='font-family:DM Mono,monospace;font-size:0.7rem;color:#6c63ff;'>Roll: {student['roll']}</div></div>",unsafe_allow_html=True)
            with dc2:
                grade=student.get('predicted_grade','—');gc=COLORS.get(grade,'#4a4a6a')
                st.markdown(f"<div style='background:#0d0d18;border:1px solid #1a1a2e;border-radius:12px;padding:1.2rem;text-align:center;'><div style='font-family:DM Mono,monospace;font-size:0.55rem;color:#2a2a4a;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:8px;'>Predicted Grade</div><div style='font-size:2.5rem;font-weight:800;color:{gc};'>{grade if grade else '—'}</div></div>",unsafe_allow_html=True)
            with dc3:
                risk=student.get('risk_level','—');rc={'Low':'#4ade80','Medium':'#fbbf24','High':'#f87171'}.get(risk,'#4a4a6a');rb={'Low':'#0d2b1a','Medium':'#2b2200','High':'#2b0a0a'}.get(risk,'#0d0d18')
                st.markdown(f"<div style='background:#0d0d18;border:1px solid #1a1a2e;border-radius:12px;padding:1.2rem;text-align:center;'><div style='font-family:DM Mono,monospace;font-size:0.55rem;color:#2a2a4a;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:8px;'>Risk Level</div><div style='background:{rb};color:{rc};border:1px solid {rc}40;padding:6px 16px;border-radius:999px;font-family:DM Mono,monospace;font-size:0.8rem;font-weight:600;display:inline-block;'>{risk if risk else '—'}</div></div>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown(stt("Your academic data — read only"),unsafe_allow_html=True)
            st.markdown("<div style='font-family:DM Mono,monospace;font-size:0.65rem;color:#f87171;margin-bottom:1rem;'>⚠ This data is managed by your faculty. You cannot modify it.</div>",unsafe_allow_html=True)
            fields=[("Attendance Rate","attendance","%"),("Assignment Average","assignment_avg","%"),("Midterm Score","midterm_score","%"),("Quiz Average","quiz_avg","%"),("Late Submissions","late_submissions",""),("Study Hours/Week","study_hours"," hrs")]
            fc1,fc2=st.columns(2)
            for idx,(label,key,suffix) in enumerate(fields):
                val=student.get(key,0);color='#4ade80' if val>=70 else '#fbbf24' if val>=55 else '#f87171'
                if key in ['late_submissions','study_hours']: color='#e8e6f0'
                with (fc1 if idx%2==0 else fc2):
                    st.markdown(f"<div style='background:#0d0d18;border:1px solid #1a1a2e;border-radius:10px;padding:12px 16px;margin-bottom:10px;'><div style='font-family:DM Mono,monospace;font-size:0.58rem;color:#2a2a4a;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:6px;'>{label}</div><div style='font-size:1.4rem;font-weight:800;color:{color};'>{val}{suffix}</div><div style='height:4px;background:#1a1a2e;border-radius:2px;margin-top:8px;overflow:hidden;'><div style='width:{min(100,int(val))}%;height:100%;background:{color};border-radius:2px;'></div></div></div>",unsafe_allow_html=True)
            if student.get('predicted_grade'):
                st.markdown("<br>",unsafe_allow_html=True)
                st.markdown(stt("Skill profile vs class average"),unsafe_allow_html=True)
                vals=[student.get('attendance',0),student.get('assignment_avg',0),student.get('midterm_score',0),student.get('quiz_avg',0),min(student.get('study_hours',0)*2.5,100),max(0,100-student.get('late_submissions',0)*6.5)]
                cats=['Attendance','Assignments','Midterm','Quizzes','Study Hrs','Submission']
                fr=go.Figure()
                fr.add_trace(go.Scatterpolar(r=vals+[vals[0]],theta=cats+[cats[0]],fill='toself',fillcolor='rgba(108,99,255,0.15)',line=dict(color='#6c63ff',width=2),name='You',mode='lines+markers',marker=dict(color='#6c63ff',size=5)))
                fr.add_trace(go.Scatterpolar(r=[81,75,72,74,55,74,81],theta=cats+[cats[0]],fill='toself',fillcolor='rgba(74,222,128,0.06)',line=dict(color='#4ade80',width=1.5,dash='dot'),name='Class Avg'))
                fr.update_layout(**pc(),height=300,polar=dict(bgcolor='rgba(0,0,0,0)',angularaxis=dict(tickfont=dict(color=TC,size=10),gridcolor=GC,linecolor=GC),radialaxis=dict(tickfont=dict(color=TC,size=9),gridcolor=GC,linecolor=GC,range=[0,100])),legend=dict(font=dict(color=TC,size=10,family='DM Mono'),bgcolor='rgba(0,0,0,0)'))
                st.plotly_chart(fr,use_container_width=True,config={"displayModeBar":False})
                st.markdown(stt("Subject-wise performance"),unsafe_allow_html=True)
                base=student.get('assignment_avg',0);mid=student.get('midterm_score',0);quiz=student.get('quiz_avg',0)
                subjects={"Mathematics":round(min(100,base*0.95)),"Science":round(min(100,mid*0.98)),"English":round(min(100,base*1.10)),"History":round(min(100,base*0.85)),"Computer Science":round(min(100,quiz*1.10)),"Physics":round(min(100,mid*0.88)),"Chemistry":round(min(100,base*0.92))}
                sb1,sb2=st.columns(2)
                for idx,(subj,score) in enumerate(subjects.items()):
                    color='#4ade80' if score>=70 else '#fbbf24' if score>=55 else '#ef4444'
                    with (sb1 if idx%2==0 else sb2):
                        st.markdown(f"<div style='margin-bottom:9px;'><div style='display:flex;justify-content:space-between;font-size:0.75rem;color:#4a4a6a;font-family:DM Mono,monospace;margin-bottom:4px;'><span>{subj}</span><span style='color:#e8e6f0;font-weight:500;'>{score}%</span></div><div style='height:5px;background:#1a1a2e;border-radius:3px;overflow:hidden;'><div style='width:{score}%;height:100%;background:{color};border-radius:3px;'></div></div></div>",unsafe_allow_html=True)
                st.markdown("<br>",unsafe_allow_html=True)
                st.markdown(stt("Personalized recommendations"),unsafe_allow_html=True)
                tips=[]
                if student.get('attendance',0)<75: tips.append("Attendance is below 75% — attend all remaining classes immediately.")
                if student.get('late_submissions',0)>5: tips.append("Too many late submissions — use a weekly planner.")
                if student.get('midterm_score',0)<60: tips.append("Mid-term score is low — visit office hours and attempt mock tests.")
                if student.get('assignment_avg',0)<65: tips.append("Assignment average is weak — join peer study groups.")
                if student.get('study_hours',0)<10: tips.append("Increase study hours to at least 12–15 hours per week.")
                if student.get('quiz_avg',0)<60: tips.append("Quiz average is low — revise past quizzes regularly.")
                if not tips: tips.append("Great performance! Keep maintaining your study habits.")
                rc1,rc2=st.columns(2)
                for i,tip in enumerate(tips):
                    with (rc1 if i%2==0 else rc2): st.markdown(f"<div class='rc'>→ {tip}</div>",unsafe_allow_html=True)

    # ══ MANAGE USERS ══════════════════════════════════════
    elif page=="👥 Manage Users":
        if not can_access(["admin"]): access_denied()
        else: show_manage_users()