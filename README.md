# IA898
Conjunto de funções utilizadas no curso IA898 - Processamento Digital de Imagens

Criado primeira vez no curso do 1º semestre 2017

## Instalação

- faça o clone do repositório
- abra o jupyter e execute o notebook ia898/src/GenerateLibrary

## Dependência:
    - numpy
    - matplotlib
    - jupyter and jupyter extentions

## Lessons
- [chess](master/chess.ipynb) - Illustrate the many ways to create an image of a chess like template
- iauint8pitfalls- Common errors processing uint8 data
- iagenimages - Illustrate the generation of different images
- iaprofiledemo - Illustrate the extraction and plotting of a profile
- [gengaussian](master/gengaussian.ipynb) - Illustrate the generation of d-dimensional Gaussian image
- iait - Illustrate the contrast transform function
- iahisteq - Illustrate how to make a histogram equalization
- [corrdemo](master/corrdemo.ipynb) - Illustrate the Template Matching technique
- iaphasecorrdemo - Illustrate the phase correlation technique
- iadftdecompose - Illustrate the decomposition of the image in primitive 2-D waves.
- iacosdemo - Illustrate discrete cosine wave and its DFT showing its periodic nature.
- iadftexamples - Demonstrate the DFT spectrum of simple synthetic images.
- iadftmatrixexamples - Demonstrate the kernel matrix for the DFT Transform.
- [dftscaleproperty](master/dftscaleproperty.ipynb) - Illustrate the scale property of the Discrete Fourier Transform.
- iaconvteo - Illustrate the convolution theorem
- iahotelling - Illustrate the Hotelling Transform
- iainversefiltering - Illustrate the inverse filtering for restoration.
- [magnify](master/magnify.ipynb) - Illustrate the interpolation of magnified images
- iamosaicdemo - Illustrate the use of mosaic to show 3D images
- iaotsudemo - Illustrate the Otsu Thresholding Selection Method

## Images
- iaimages - Images available to use in examples.
- iareadurl - Read image from URL path.

## Halftoning Approximation
- iadither - Ordered Dither.
- iafloyd - Floyd-Steinberg error diffusion.

## Color Processing
- iaapplylut - Intensity image transform.
- iacolormap - Create a colormap table.
- iatcrgb2ind - True color RGB to index image and colormap.
- iargb2gray - Convert True color RGB to gray image (luminance).

## Geometric Manipulations
- [affine](src/affine.ipynb) - Affine transform. Supports 3D but no interpolation.
- iaffine3 - Enhanced Affine transform. Supports 3D transforms, color images and linear interpolation.
- iageorigid - 2D Rigid body geometric transformation and scaling.
- [polar](src/polar.ipynb) - Cartesian to polar coordinate transformation.
- [ptrans](src/ptrans.ipynb) - Periodic translation.
- iarot90 - 3D 90-degree rotation

## Image Filtering
- iabwlp - Low-Pass Butterworth frequency filter.
- ialogfilter - Laplacian of Gaussian filter.
- iacontour - Contours of binary images.
- [conv](src/conv.ipynb) - 2D or 3D convolution.
- [pconv](src/pconv.ipynb) - 2D or 3D periodic convolution (kernel origin at center of kernel).
- iapconv2 - 1D, 2D or 3D periodic convolution (kernel origin at array origin).
- iasobel - Sobel edge detection.
- iavarfilter - Variance filter.

## Automatic Thresholding Techniques
- iaotsu - Thresholding by Otsu.

## Visualization
- adshow - Basic display image in Adessowiki.
- iamosaic - Creates a mosaic of images from the input volume (3D).
- iagshow - Overlay color planes on a gray scale image ready for display.
- ialblshow - Display a labeled image assigning a random color for each label.
- ianshow - Image graphic representation useful for illustration, accepts overlay color planes.
- iaisolines - Isolines of a grayscale image.
- iadftview - Generate optical Fourier Spectrum for display from DFT data.
- iatiling - Create a large 2D image from a list of smaller images.
- iafig2img - Convert a matplotlib figure to an image ready to be displayed by adshow.
- iaplot - Simple plotting ready to be displayed adshow.
- iashow - Image display. DO NOT USE. Use adshow instead.

## Image Information and Manipulation
- iaroi - Cut a rectangle out of an image.
- iacrop - Crop an image to find the minimum rectangle.
- iapad - Extend the image inserting a frame around it.
- iaimginfo - Print image size and pixel data type information
- iaind2sub - Convert linear index to double subscripts.
- [meshgrid](src/meshgrid.ipynb) - Create two 2-D matrices of indexes.
- ianeg - Negate an image.
- normalize - Normalize the pixels values between the specified range.
- iasub2ind - Convert linear double subscripts to linear index.

## Image Transformation
- iadct - Discrete Cossine Transform.
- iadctmatrix - Kernel matrix for the DCT Transform.
- iadft - Discrete Fourier Transform.
- iadftmatrix - Kernel matrix for the DFT Transform.
- iafftshift - Shifts zero-frequency component to center of spectrum.
- iaifftshift - Undoes the effects of iafftshift.
- haarmatrix - Kernel matrix for the Haar Transform.
- [hadamard](src/hadamard.ipynb) - Hadamard Transform.
- [hadamardmatrix](src/hadamardmatrix.ipynb) - Kernel matrix for the Hadamard Transform.
- iahwt - Haar Wavelet Transform.
- iaidct - Inverse Discrete Cossine Transform.
- iaidft - Inverse Discrete Fourier Transform.
- [ihadamard](src/ihadamard.ipynb) - Inverse Hadamard Transform.
- iaihwt - Inverse Haar Wavelet Transform.
- iaisdftsym - Check for conjugate symmetry
- [pca](src/pca.ipynb) - Principal Component Analysis

## Measurements
- histogram - Image histogram.
- iah2stats - Image statistics from its histogram.
- iastat - Calculates MSE, PSNR and Pearson correlation between two images.
- iacolorhist - Color-image histogram.
- iapercentile - Computes the percentile from the image.
- iah2percentile - Computes the percentile from the histogram.

## Image Creation
- iacircle - Create a binary circle image.
- iaramp - Create an image with vertical bands of increasing gray values.
- iacos - Create a cosine wave image.
- iagaussian - Generate a n-dimensional Gaussian image.
- [ellipse](src/ellipse.ipynb) - Generate a 2D ellipse, rectangle or diamond image.
- [log](src/log.ipynb) - Laplacian of Gaussian image.
- [comb](src/comb.ipynb) - Create a grid of impulses image.
- iarectangle - Create a binary rectangle image.
- iatext - Create a binary image of a text.

## Interpolation
- iainterpolclosest - Closest pixel interpolation
- iainterpollin - Linear, bi-linear or tri-linear interpolation

## Image Matching
- iacorr - Simple correlation between two images of the same size
- [phaseorr](src/phasecorr.ipynb) - Phase correlation
- iawcorr - Weighted correlation between two images of the same size
