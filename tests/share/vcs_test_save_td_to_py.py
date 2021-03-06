#####################################
#                                 #
# Import and Initialize VCS     #
#                             #
#############################
import vcs
v=vcs.init()

#----Taylordiagram (Gtd) 
gtd_list=v.listelements('taylordiagram')
if ('vcs_test_save_taylor_to_json_and_python' in gtd_list):
   __Gtd__vcs_test_save_taylor_to_json_and_python = v.gettaylordiagram('vcs_test_save_taylor_to_json_and_python')
else:
   __Gtd__vcs_test_save_taylor_to_json_and_python = v.createtaylordiagram('vcs_test_save_taylor_to_json_and_python')
__Gtd__vcs_test_save_taylor_to_json_and_python.detail = 75
__Gtd__vcs_test_save_taylor_to_json_and_python.max = None
__Gtd__vcs_test_save_taylor_to_json_and_python.quadrans = 1
__Gtd__vcs_test_save_taylor_to_json_and_python.skillValues = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95]
__Gtd__vcs_test_save_taylor_to_json_and_python.skillColor = 252
__Gtd__vcs_test_save_taylor_to_json_and_python.skillDrawLabels = 'y'
__Gtd__vcs_test_save_taylor_to_json_and_python.skillCoefficient = [1.0, 1.0, 1.0]
__Gtd__vcs_test_save_taylor_to_json_and_python.referencevalue = 1.0
__Gtd__vcs_test_save_taylor_to_json_and_python.arrowlength = 0.05
__Gtd__vcs_test_save_taylor_to_json_and_python.arrowangle = 20.0
__Gtd__vcs_test_save_taylor_to_json_and_python.arrowbase = 0.75
__Gtd__vcs_test_save_taylor_to_json_and_python.addMarker(
    status = 1,
    line = None,
    id = '0',
    id_size = 20,
    id_color = 16,
    id_font = 1,
    symbol = 'dot',
    color = 16,
    size = 5,
    xoffset = 2.0380499362945557,
    yoffset = 1.0833240747451782,
    line_color = [0.0, 0.0, 0.0, 100.0],
    line_size = 1.0,
    line_type = 'solid'
)
__Gtd__vcs_test_save_taylor_to_json_and_python.addMarker(
    status = 1,
    line = None,
    id = '1',
    id_size = 20,
    id_color = 239,
    id_font = 1,
    symbol = 'dot',
    color = 239,
    size = 5,
    xoffset = 2.1889517307281494,
    yoffset = 1.5037295818328857,
    line_color = [0.0, 0.0, 0.0, 100.0],
    line_size = 1.0,
    line_type = 'solid'
)
__Gtd__vcs_test_save_taylor_to_json_and_python.addMarker(
    status = 1,
    line = None,
    id = '2',
    id_size = 20,
    id_color = 16,
    id_font = 1,
    symbol = 'dot',
    color = 16,
    size = 5,
    xoffset = 2.005732774734497,
    yoffset = 1.2790908813476562,
    line_color = [0.0, 0.0, 0.0, 100.0],
    line_size = 1.0,
    line_type = 'solid'
)
__Gtd__vcs_test_save_taylor_to_json_and_python.addMarker(
    status = 1,
    line = None,
    id = '3',
    id_size = 20,
    id_color = 239,
    id_font = 1,
    symbol = 'dot',
    color = 239,
    size = 5,
    xoffset = 2.194457530975342,
    yoffset = 1.4414606094360352,
    line_color = [0.0, 0.0, 0.0, 100.0],
    line_size = 1.0,
    line_type = 'solid'
)
__Gtd__vcs_test_save_taylor_to_json_and_python.addMarker(
    status = 1,
    line = None,
    id = '4',
    id_size = 30,
    id_color = 1,
    id_font = 1,
    symbol = 'dot',
    color = 1,
    size = 5,
    xoffset = 0.0,
    yoffset = 0.0,
    line_color = [0.0, 0.0, 0.0, 100.0],
    line_size = 1.0,
    line_type = 'solid'
)
