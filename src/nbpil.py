"""
    Module nbpil -- Toolbox nbpil - notebook interface com PIL
    -------------------------------------------------------------------
    This module provides a link between numpy arrays and PIL, Python Imaging
    Library, images. Its functions perform image file I/O (in formats supported
    by PIL) and displaying of images represented as numpy arrays. The layout
    of these numpy arrays follows the rules of the adimage toolbox images.
    -------------------------------------------------------------------
    nbimages()    -- List image files located on sys.imagepath, if this variable
                     exists, or, otherwise, on sys.path
    nbread()      -- Read an image from a file to a numpy array.
    nbshow()      -- Display an image
    nbwrite()     -- Write an image from a numpy array to an image file. The
                     format is deduced from the filename extension.
    array2pil()   -- Convert a numpy array to a PIL image
    pil2array()   -- Convert a PIL image to a numpy array

"""
#
__version__ = '0.8 all'

__version_string__ = 'Toolbox nbpil V0.8 8Jan2017'

#
# =====================================================================
#
#   Global statements for adread
#
# =====================================================================
def findImageFile(filename):
    '''Search image filename in sys.imagepath or sys.path.'''
    import sys, os.path
    if not os.path.isfile(filename) and not os.path.isabs(filename):
        try:
            for a in sys.imagepath:
                if os.path.isfile(os.path.join(a, filename)):
                    filename = os.path.join(a, filename)
                    break
        except:
            for a in sys.path:
                if os.path.isfile(os.path.join(a, filename)):
                    filename = os.path.join(a, filename)
                    break
    return filename
# =====================================================================
#
#   nbread
#
# =====================================================================
def nbread(imagefile):
    """
        - Purpose
            Read an image from a file to a numpy array.
        - Synopsis
            arr = nbread(imagefile)
        - Input
            imagefile: Image file path.
        - Output
            arr: numpy array representing an image.

    """

    from PIL import Image
    img = findImageFile(imagefile)
    arr = pil2array(Image.open(img))
    return arr
#
# =====================================================================
#
#   nbreadgray
#
# =====================================================================
def nbreadgray(imagefile):
    """
        - Purpose
            Read an image from a file to a numpy array as grayscale.
        - Synopsis
            arr = nbread(imagefile)
        - Input
            imagefile: Image file path.
        - Output
            arr: numpy array representing an image.

    """
    
    from PIL import Image
    img = findImageFile(imagefile)
    arr = pil2array(Image.open(img).convert('L'))
    return arr
#
# =====================================================================
#
#   nbwrite
#
# =====================================================================
def nbwrite(imagefile, arr):
    """
        - Purpose
            Write an image from a numpy array to an image file. The format
            is deduced from the filename extension.
        - Synopsis
            nbwrite(imagefile, arr)
        - Input
            imagefile: Image file path.
            arr:       The numpy array to save.

    """

    array2pil(arr).save(imagefile)
    return
#
# =====================================================================
#
#   Global statements for nbimages
#
# =====================================================================
def listImageFiles(glb='*'):
    '''List image files located on sys.path.'''
    import sys, os.path, glob
    if os.path.splitext(glb)[1] == '':
        imgexts = ['.tif', '.jpg', '.gif', '.png', '.pbm', '.pgm', '.ppm', '.bmp']
    else:
        imgexts = ['']
    images = {}
    try:
        for dir in sys.imagepath:
            for ext in imgexts:
                for ff in glob.glob(os.path.join(dir, glb + ext)):
                    images[os.path.basename(ff)] = ff
    except:
        for dir in sys.path:
            for ext in imgexts:
                for ff in glob.glob(os.path.join(dir, glb + ext)):
                    images[os.path.basename(ff)] = ff
    return images
# =====================================================================
#
#   nbimages
#
# =====================================================================
def nbimages(glob='*'):
    """
        - Purpose
            List image files located on sys.imagepath, if this variable
            exists, or, otherwise, on sys.path
        - Synopsis
            imglist = nbimages(glob='*')
        - Input
            glob: Default: '*'. Glob string for the image filename.
        - Output
            imglist: Image filename list.

    """

    lst = listImageFiles(glob).keys()
    lst.sort()
    return lst

# =====================================================================
#
#   nbshow
#
# =====================================================================

from cStringIO import StringIO
import IPython.display
import numpy as np
from PIL import Image
def nbshow_old(a, title=None, fmt='png', width=None):
    if a.dtype == bool:
        a = np.uint8(a) * 255
    elif a.dtype != np.uint8:
        raise ValueError('Accept only bool ou uint8 image. It was %s' % a.dtype) 
    f = StringIO()
    #print(dtype,a.shape,a.max(),a.min()
    fi = Image.fromarray(a)
    fi.save(f, fmt)
    if width:
        IPython.display.display(IPython.display.Image(width=width,data=f.getvalue()))
    else:
        IPython.display.display(IPython.display.Image(data=f.getvalue()))
    if title:
        print(title)

from cStringIO import StringIO
from IPython.display import display, Image, HTML
import base64
import numpy as np
import PIL

class nbshow:
    #constructor
    def __init__(self, ncols = 3,width = [], fmt = 'png'):
        self.imgs = []
        self.titles = []
        self.ncols = ncols
        self.width = []   
        self.fmt = fmt
        return
    #sets figure size. Ex figsize = (12,8)
    def set_figsize(self,figsize):
        self.figsize = figsize
        return
    #sets image width
    def set_width(self,width):
        self.width = width
        return    
    #displays image in subplot format 
    #append images to list of images to be displayed
    def nbshow(self,img=None,title = ""):
        if img is not None:
            self.imgs.append(img)
            self.titles.append(title)
        else: 
            number_of_subplots = len(self.imgs)
            imagesList = "<head><style>\
                table, th, td { border: 0px solid black;\
                text-align: center;border-collapse: collapse;}</style></head>\
                <body><table border=\"0\">"
            for i,(img,title) in enumerate(zip(self.imgs,self.titles)): 
                if i%self.ncols == 0:
                    imagesList += "<tr>"
                if img.dtype == bool:
                    img = np.uint8(img) * 255
                elif img.dtype != np.uint8:
                    raise ValueError('Accept only bool ou uint8 image. It was %s' % img.dtype) 
                f = StringIO()
                fi = PIL.Image.fromarray(img)
                fi.save(f, self.fmt)
                imgbuffer = f.getvalue()
                img_b64 = base64.b64encode(imgbuffer)
                imagesList +="<td>\
                    <table><tr><td><img src='data:image/png;base64,%s'/></td></tr>\
                    <tr><td align='center'>%s</td></tr></table></td>" % (img_b64,title)
                if i%self.ncols == (self.ncols-1):
                    imagesList += "<tr>"
            imagesList +="</tr></table></body>"
            # empties buffer
            self.imgs = []
            self.titles = []
            #print 'imagelist:',imagesList
            display(HTML(imagesList))

#
# =====================================================================
#
#   pil2array
#
# =====================================================================

def PIL2array(img):
    return np.array(img.getdata(),
                    np.uint8).reshape(img.size[1], img.size[0], 3)


def pil2array(pil):
    """
        - Purpose
            Convert a PIL image to a numpy array
        - Synopsis
            arr = pil2array(pil)
        - Input
            pil: The PIL image to convert.
        - Output
            arr: numpy array representing the PIL image.
        - Description
            Convert a PIL image to a numpy array. The array representing a
            RGB(A) image is formed by images stored sequencially: R-image,
            G-image, B-image and, optionally, Alpha-image.

    """

    import numpy
    w, h = pil.size
    binary = 0
    if pil.mode == '1':
        binary = 1
        pil = pil.convert('L')
    if pil.mode == 'L':
        d = 1 ; shape = (h,w)
    elif pil.mode == 'P':
        if 0:   # len(pil.palette.data) == 2*len(pil.palette.rawmode):
            binary = 1
            pil = pil.convert('L')
            d = 1 ; shape = (h,w)
        else:
            pil = pil.convert('RGB')
            d = 3 ; shape = (h,w,d)
    elif pil.mode in ('RGB','YCbCr'):
        d = 3 ; shape = (h,w,d)
    elif pil.mode in ('RGBA','CMYK'):
        d = 4 ; shape = (h,w,d)
    else:
        raise TypeError, "Invalid or unimplemented PIL image mode '%s'" % pil.mode
    arr = numpy.reshape(numpy.fromstring(pil.tobytes(), 'B', w*h*d), shape)
    #if d > 1:
    #    arr = numpy.swapaxes(numpy.swapaxes(arr, 0, 2), 1, 2)
    if binary:
        arr = arr.astype('?')
    return arr
#
# =====================================================================
#
#   array2pil
#
# =====================================================================
def array2PIL(arr, size):
    mode = 'RGBA'
    arr = arr.reshape(arr.shape[0]*arr.shape[1], arr.shape[2])
    if len(arr[0]) == 3:
        arr = numpy.c_[arr, 255*numpy.ones((len(arr),1), numpy.uint8)]
    return Image.frombuffer(mode, size, arr.tostring(), 'raw', mode, 0, 1)


def array2pil(arr):
    """
        - Purpose
            Convert a numpy array to a PIL image
        - Synopsis
            pil = array2pil(arr)
        - Input
            arr: numpy array to convert.
        - Output
            pil: The resulting PIL image.
        - Description
            Convert a numpy array to a PIL image. Use the conventions
            explained in the pil2array docstring.

    """
    from PIL import Image
    nd = len(arr.shape)
    x = arr.astype('B')
    if nd == 2:
        d, h, w = (1,) + arr.shape
        mode = 'L'
    elif nd == 3:
        if arr.dtype.char == '?':
            raise TypeError, "Binary array cannot be RGB"
        d, h, w = arr.shape
        if   d == 1: mode = 'L'
        elif d == 3: mode = 'RGB'
        elif d == 4: mode = 'RGBA'
        else:
            raise TypeError, "Array first dimension must be 1, 3 or 4 (%d)" % d
    else:
        raise TypeError, "Array must have 2 or 3 dimensions (%d)" % nd
    #if d > 1:
    #    x = numpy.swapaxes(numpy.swapaxes(x, 1, 2), 0, 2)
    pil = Image.frombytes(mode, (w,h), x.tobytes())
    if arr.dtype.char == '?':
        pil = pil.point(lambda i: i>0, '1')
    return pil


