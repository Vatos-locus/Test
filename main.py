import webbrowser
import ctypes
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)


volume = cast(interface, POINTER(IAudioEndpointVolume))

volume_range = volume.GetVolumeRange()
max_volume = volume_range[1]

volume.SetMasterVolumeLevel(max_volume, None)



def rickroll():
    url = 'https://www.youtube.com/watch?v=a3Z7zEc7AXQ'
    webbrowser.open(url)

rickroll()


