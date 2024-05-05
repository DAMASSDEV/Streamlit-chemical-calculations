import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu


with st.sidebar:
    st.image('https://github.com/DAMASSDEV/Streamlit-chemical-calculations/blob/main/Assets/Foto_Judul.jpg')
    st.title('WELCOME TO PROGRAM')
    st.subheader("KELOMPOK 2")
    Selected = option_menu('Menu',['Program Aplikasi Perhitungan μ VT', 'Program Aplikasi Perhitungan μ FP'])

if Selected == "Program Aplikasi Perhitungan μ VT":
    def apet():
        st.title('Aplikasi Perhitungan μ ET')
        volume_rata_rata_ml = st.number_input('Masukkan nilai volume rata-rata(mL)',value=None, placeholder="Ketikan angka...")
        st.write(volume_rata_rata_ml)
        delta_suhu = st.number_input('Masukkan nilai delta suhu(℃)',value=None,placeholder="Ketikkan angka...")
        st.write(delta_suhu)
        koefisien_muai_air = st.number_input('Masukkan nilai koefisien muai air(℃)',value=None,placeholder='Ketikkan angka...')
        st.write(koefisien_muai_air)  
            
        tombol = st.button('Hitung nilai μ ET(mL)')
        if tombol:
                nilai_μ_ET = (volume_rata_rata_ml*delta_suhu*koefisien_muai_air)/1.73205
                st.success(f"Nilai μ ET adalah {nilai_μ_ET}")
                st.balloons()


    def apven():
        st.title('Aplikasi Perhitungan μ Vendpoit')
        skala_terkecil_buret_ml = st.number_input("Masukkan nilai skala terkecil buret(mL)",value=None,placeholder="Ketikkan angka...")
        st.write(skala_terkecil_buret_ml)
        delta_suhu = st.number_input('Masukkan nilai delta suhu(℃)',key="delta_suhu_2",value=None,placeholder="Ketikkan angka...")
        st.write(delta_suhu)
        koefisien_muai_air = st.number_input('Masukkan nilai koefisien muai air(℃)',key="Koef_2",value=None,placeholder='Ketikkan angka...')
        st.write(koefisien_muai_air)

        tombol = st.button("Hitung nilai μ Vendpoit(mL)")
        if tombol:
            nilai_μ_Vendpoit = (skala_terkecil_buret_ml*delta_suhu*koefisien_muai_air)/1.73205
            st.success(f"Nilai μ Vendpoit adalah {nilai_μ_Vendpoit}")
            st.balloons()
    def apvt():
        st.title('Aplikasi Perhitungan μ Volume Titran')
        kalibrasi_buret_mL = st.number_input('Masukkan nilai μ kalibrasi buret(mL)',value=None,placeholder="Ketikkan angka...")
        st.write(kalibrasi_buret_mL)
        ET_mL = st.number_input('Masukkan nilai μ ET(mL)',value=None,placeholder="Ketikkan angka...")
        st.write(ET_mL)
        Vendpoint = st.number_input('Masukkan nilai μ Vendpoint(mL)',value=None,placeholder="Ketikkan angka...")
        st.write(Vendpoint)

        tombol = st.button('Hitung nilai μ Vtitran(mL)')
        if tombol:
                    nilai_μ_Vtitran = (((kalibrasi_buret_mL)*2)+((ET_mL)*2)+(((Vendpoint))*2))*0.5
                    st.success(f"Nilai μ Vtitran adalah {nilai_μ_Vtitran}")
                    st.balloons()

    
    tab1,tab2,tab3 = st.tabs(['Perhitungan μ ET', 'Perhitungan μ Vendpoint', 'Perhitungan μ VT'])
    with tab1:
         tab1.write(apet())
    with tab2:
         tab2.write(apven())
    with tab3:
         tab3.write(apvt())

if Selected == 'Program Aplikasi Perhitungan μ FP':
    def hitung8():
        st.title('Aplikasi Perhitungan μ pipet')

        miu_kal_pipet_mL = st.number_input("Masukan nilai μ kalibrasi pipet(mL)",value=None, placeholder='Ketikkan angka...' )
        st.write(miu_kal_pipet_mL)
        volume_pipet_mL = st.number_input("Masukan nilai volume pipet(mL)",value=None, placeholder='Ketikkan angka...' )
        st.write(volume_pipet_mL)
        delta_suhu_3 = st.number_input("Masukan nilai delta suhu(℃)",value=None, placeholder='Ketikkan angka...')
        st.write(delta_suhu_3)
        koefisien_muai_air_3 = st.number_input("koefisien muai air(℃)",value=None, placeholder='Ketikkan angka....')
        st.write(koefisien_muai_air_3)
        

        tombol = st.button("Hitung nilai μ pipet(mL)")

        if tombol:
            nilai_μ_pipet = (((miu_kal_pipet_mL/1.73205)*2)+((volume_pipet_mL*delta_suhu_3*koefisien_muai_air_3/1.73205)*2))*0.5
            st.success(f"Nilai μ pipet adalah {nilai_μ_pipet}")
            st.balloons()

    def hitung3():
        st.title('Aplikasi Perhitungan μ labu takar')

        miu_kal_labu_takar_mL = st.number_input("Masukan nilai μ kalibrasi labu takar(mL)",value=None,key="miu_kal_labu_takar_mL", placeholder='Ketikkan angka...' )
        st.write(miu_kal_labu_takar_mL)
        volume_labu_takar_mL_2 = st.number_input("Masukan nilai volume labu takar(mL)",value=None,key="miu_kal_labu_takar_",placeholder='Ketikkan angka...' )
        st.write(volume_labu_takar_mL_2)
        delta_suhu_4 = st.number_input("Masukan nilai delta suhu(℃)",value=None,key="miu_kal_labu_takas",placeholder='Ketikkan angka...')
        st.write(delta_suhu_4)
        koefisien_muai_air_4 = st.number_input("koefisien muai air(℃)",value=None,key="miu_kal_labu_takar_mLs",placeholder='Ketikkan angka....')
        st.write(koefisien_muai_air_4)
        

        tombol = st.button("Hitung nilai μ labu takar(mL)")

        if tombol:
            nilai_μ_labu_takar = (((miu_kal_labu_takar_mL/1.73205)*2)+((volume_labu_takar_mL_2*delta_suhu_4*koefisien_muai_air_4/1.73205)*2))*0.5
            st.success(f"Nilai μ labu takar adalah {nilai_μ_labu_takar }")
            st.balloons()

    def hitung4():
        st.title('Aplikasi Perhitungan μ FP')

        faktor_pengali_2 = st.number_input("Masukan nilai Faktor pengali",value=None, placeholder='Ketikkan angka...' )
        st.write(faktor_pengali_2)    
        miu_labu_takar = st.number_input("Masukan nilai μ labu takar",value=None, placeholder='Ketikkan angka...' )
        st.write(miu_labu_takar)
        miu_ET_mL_2= st.number_input("Masukan nilai μ ET(mL)",value=None, placeholder='Ketikkan angka...')
        st.write(miu_ET_mL_2)
    
        tombol = st.button("Hitung nilai μ Vtitran(mL)")

        if tombol:
            nilai_μ_FP = faktor_pengali_2*(((miu_labu_takar)*2)+((miu_ET_mL_2)*2))*0.5
            st.success(f"Nilai μ FP adalah {nilai_μ_FP}")
            st.balloons()


    tab1,tab2,tab3 = st.tabs(["Perhitungan μ pipet", "Perhitungan μ labu takar","Perhitungan μ FP"])
    with tab1:
        tab1.write(hitung8())
    with tab2:
        tab2.write(hitung3())
    with tab3:
        tab3.write(hitung4())
