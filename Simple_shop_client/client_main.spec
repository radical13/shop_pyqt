# -*- mode: python -*-

block_cipher = None


a = Analysis(['client_main.py'],
             pathex=['/Users/hushiyang/Documents/documents/2017.9秋季学期/数据通信与计算机网络/PJ/shop_pyqt/Simple_shop_client'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='client_main',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
app = BUNDLE(exe,
             name='client_main.app',
             icon=None,
             bundle_identifier=None)
