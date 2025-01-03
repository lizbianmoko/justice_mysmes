#************************************
# CGs
#************************************

# CGs are automatically resized in the chatroom, but you have to
# make sure the original dimensions are 750x1334
# The name of the cg must be "cg " + the name of the album minus
# "album" e.g. ju_album -> "ju", common_album -> "common"
# + a number or some other indicator of what the image is
image cg common_1 = "CGs/common_album/cg-1.webp"
image cg common_2 = "CGs/common_album/cg-2.webp"
image cg common_3 = "CGs/common_album/cg-3.webp"

image cg s_1 = "CGs/s_album/cg-1.webp"

image cg r_1 = "CGs/r_album/cg-1.webp"

image cg ju_1 = "CGs/ju_album/cg-1.webp"


#************************************
# Album Cover Images
#************************************
image cg_label_common = 'CGs/label_bg_common.webp'
image cg_label_ja = 'CGs/label_bg_ja.webp'
image cg_label_ju = 'CGs/label_bg_ju.webp'
image cg_label_other = 'CGs/label_bg_other.webp'
image cg_label_r = 'CGs/label_bg_r.webp'
image cg_label_s = 'CGs/label_bg_s.webp'
image cg_label_u = 'CGs/label_bg_u.webp'
image cg_label_v = 'CGs/label_bg_v.webp'
image cg_label_y = 'CGs/label_bg_y.webp'
image cg_label_z = 'CGs/label_bg_z.webp'

image ja_album_cover = 'CGs/ja_album_cover.webp'
image ju_album_cover = 'CGs/ju_album_cover.webp'
image r_album_cover = 'CGs/r_album_cover.webp'
image s_album_cover = 'CGs/s_album_cover.webp'
image u_album_cover = 'CGs/u_album_cover.webp'
image v_album_cover = 'CGs/v_album_cover.webp'
image y_album_cover = 'CGs/y_album_cover.webp'
image z_album_cover = 'CGs/z_album_cover.webp'
image common_album_cover = 'CGs/common_album_cover.webp'


#************************************
# Album Declarations
#************************************
init offset = 1000
## In order to allow for albums to be easily expanded,
## these constants are used. This is where you actually
## declare all of the Album objects you need.
define ja_album = [ ]
define ju_album = [ ]
define r_album = [ GalleryImage("cg r_1") ]
define s_album = [ GalleryImage("cg s_1") ]
define u_album = []
define v_album = []
define y_album = []
define z_album = []
define common_album = [
    GalleryImage("cg common_1"),
    GalleryImage("cg common_2"),
    GalleryImage("cg common_3")
]


init offset = 0

# This list allows the program to automatically manage the albums available
# in the album gallery.
# It should contain the letter before _album in the album definition; if
# the album is not associated with a particular character its title will
# be whatever this string is (so 'common' shows as "Common" in the Album).
default all_albums = [
    'ju', 'z', 's', 'y', 'ja', 'v', 'u', 'r', 'common'
]