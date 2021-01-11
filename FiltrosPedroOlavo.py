import numpy as np
import cv2
import streamlit as st
from PIL import Image, ImageEnhance

output_width = 500
our_image = Image.open("baixados.jpeg")
def main():
    our_image = Image.open("baixados.jpeg")
    st.title("Aplicação para teste de filtros")
    st.text("Feito por Pedro Olavo")
    st.sidebar.title("Opções")

    #menu com opções de página
    opcoes_menu = ["Filtros", "Sobre"]
    escolha = st.sidebar.selectbox("Escolha uma opção", opcoes_menu)


    if escolha == "Filtros":

        #carregar e exibir imagem
        #our_imagem = cv2.imread('nome_da_imagem') não dá certo
        st.subheader('Faça upload de alguma imagem.')
        image_file = st.file_uploader("Carregue sua imagem e escolha um filtro aplicável no menu lateral.", type=['jpg', 'png', 'jpeg'])
        if image_file is not None:
            our_image = Image.open(image_file)
            st.sidebar.text("Imagem Inicial")
            st.sidebar.image(our_image, width=150)

        col1, col2 = st.beta_columns(2)

        #filtros que podem ser aplicados
        filtros = st.sidebar.radio("Filtros", ['Original', 'Greyscale', 'Sketch', 'Contraste',
                                               'Sépia', 'Movimento/Borrado', 'Canny'])

        if filtros == 'Greyscale':
            #converto a imagem para RBG sempre
            im_conver = np.array(our_image.convert('RGB'))
            img_cinza = cv2.cvtColor(im_conver, cv2.COLOR_RGB2GRAY)
            col1.header('Original')
            col1.image(our_image, use_column_width=True)
            col2.header('Escala de cinza')
            col2.image(img_cinza, use_column_width=True)
            #st.image(img_cinza, width=output_width)

        if filtros == 'Original':
            st.text('Imagem Original')
            st.image(our_image, width=output_width)

        if filtros == 'Contraste':
            st.text('Escolha, na escala deslizando do lado esquerdo, o constraste a ser aplicado na sua imagem.')
            c_amount = st.sidebar.slider("Contraste", 0.0, 2.0, 1.0)
            enchancer = ImageEnhance.Contrast(our_image)
            img_c = enchancer.enhance(c_amount)
            col1.header('Original')
            col1.image(our_image, use_column_width=True)
            col2.header('Constraste')
            col2.image(img_c, use_column_width=True)
            #st.image(img_c, width=output_width)

        if filtros == 'Sketch':
            im_conver = np.array(our_image.convert('RGB'))
            #passo a imagem para cinza
            im_cinza = cv2.cvtColor(im_conver, cv2.COLOR_BGR2GRAY)
            #inverto o cinza da imagem
            inv_im_cinza = 255 - im_cinza
            #faço uma imagem borrada
            im_blur = cv2.GaussianBlur(inv_im_cinza, (21, 21), 0, 0)
            im_sketch = cv2.divide(im_cinza, 255 - im_blur, scale=256)
            col1.header('Original')
            col1.image(our_image, use_column_width=True)
            col2.header('Sketch')
            col2.image(im_sketch, use_column_width=True)
            #st.image(im_sketch, width=output_width)

        if filtros == 'Sépia':
            im_conver = np.array(our_image.convert('RGB'))
            im_conver = cv2.cvtColor(im_conver, cv2.COLOR_RGB2BGR)
            kernel = np.array([[0.272, 0.534, 0.131],
                              [0.349, 0.868, 0.168],
                              [0.393, 0.769, 0.189]])
            out_im = cv2.filter2D(im_conver, -1, kernel)
            col1.header('Original')
            col1.image(our_image, use_column_width=True)
            col2.header('Sépia')
            col2.image(out_im, use_column_width=True)
            #st.image(out_im, channels='BGR', width=output_width)

        if filtros == 'Movimento/Borrado':
            b_amount = st.sidebar.slider("Kernel (nxn)",3, 27, 9, step=2)
            im_conver = np.array(our_image.convert('RGB'))
            kernel_motion_blur = np.zeros((15, 15))
            kernel_motion_blur[7, :] = np.ones(15)
            kernel_motion_blur = (kernel_motion_blur / b_amount)
            im_mov = cv2.filter2D(im_conver, -1, kernel_motion_blur)
            col1.header('Original')
            col1.image(our_image, use_column_width=True)
            col2.header('Imagem Borrada')
            col2.image(im_mov, use_column_width=True)
            #st.image(im_mov, width=output_width)

        #if filtros == 'Nitidez':
            #st.text("Melhora a nitidez da sua foto.")
            #im_conver = np.array(our_image.convert('RGB'))
            #kernel_sharpening_1 = np.array([[-1, -1, -1],
                                           # [-1, 9, -1],
                                           # [-1, -1, -1]])
            #im_nit = cv2.filter2D(im_conver, -1, kernel_sharpening_1)
            #st.image(im_nit, width=output_width)

        if filtros == 'Canny':
            im_conver = np.array(our_image.convert('RGB'))
            blur_image = cv2.GaussianBlur(im_conver, (11, 11), 0)
            canny_image = cv2.Canny(blur_image, 100, 150)
            col1.header('Original')
            col1.image(our_image, use_column_width=True)
            col2.header('Bordas detectadas')
            col2.image(canny_image, use_column_width=True)
            #st.image(canny_image, width=output_width)

    elif escolha == "Sobre":
        st.subheader("Este é meu primeiro projeto usando streamlit e opencv.")
        st.text("Sou o Pedro Olavo, aspirante a cientista de dados.")
        st.markdown("Se quiser conhecer mais do meu trabalho visite [meu LinkedIn](https://www.linkedin.com/in/pedro-olavo-sousa-201b9a1b0/)")

if __name__ == '__main__':
        main()


