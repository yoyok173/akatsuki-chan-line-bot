daftar_jurus = {'naga kacang':'nagakacang.txt'}
daftar_cmd = ['bye', 'gombal', 'help', 'info', 'jurus', 'tag', 'taglist', 'ougi', 'panggil', 'profil', 'so', 'mock', 'bolehkah','search']
img_url_tag = { 'bye':['https://image.ibb.co/ibvkKa/akatsukileave.jpg','https://image.ibb.co/meYGQF/akatsukileave_prev.jpg'],
            'gagal ambis':['https://image.ibb.co/hH2Msv/gagal_ngambis.jpg','https://image.ibb.co/mkb35F/gagal_ngambis_prev.jpg'],
            'alone':['https://image.ibb.co/g9OHhv/alone_prev.jpg','https://image.ibb.co/g9OHhv/alone_prev.jpg'],
            'hai':['https://image.ibb.co/hPE19a/hai.jpg','https://image.ibb.co/hPE19a/hai.jpg'],
            'disgusting':['https://image.ibb.co/cahopa/disgusting.jpg','https://image.ibb.co/gaREUa/disgusting_prev.jpg'],
            'jalan setan':['https://image.ibb.co/mPCA2v/jalansetan.jpg','https://image.ibb.co/eEiTpa/jalansetan_prev.jpg'],
            'jaga ketikan':['https://image.ibb.co/jsGRaF/ketikandijaga.jpg','https://image.ibb.co/e3vKvF/ketikandijaga_prev.jpg'],
            'kok sepi':['https://image.ibb.co/hViiNv/koksepi.jpg','https://image.ibb.co/dWHA2v/koksepi_prev.jpg'],
            'matte':['https://image.ibb.co/bXmsFF/matte.jpg','https://image.ibb.co/faLmaF/matte_prev.jpg'],
            'mecin':['https://image.ibb.co/iMUCFF/mecin.jpg','https://image.ibb.co/djJiNv/mecin_prev.jpg'],
            'moshi':['https://image.ibb.co/mbkmaF/moshi.jpg','https://image.ibb.co/i2Copa/moshi_prev.jpg'],
            'mwhaha':['https://image.ibb.co/cdwEUa/mwahaha.jpg','https://image.ibb.co/bOMEUa/mwahaha_prev.jpg'],
            'nani':['https://image.ibb.co/eNbg9a/nani.jpg','https://image.ibb.co/moA8pa/nani_prev.jpg'],
            'NO':['https://image.ibb.co/bSDiNv/NO.jpg','https://image.ibb.co/jgrEUa/NO_prev.jpg'],
            'NOOO':['https://image.ibb.co/dtschv/NOOO.jpg','https://image.ibb.co/dtschv/NOOO.jpg'],
            'pintar':['https://image.ibb.co/kOnShv/pintar.jpg','https://image.ibb.co/iFhGaF/pintar_prev.jpg'],
            'rasenggan':['https://image.ibb.co/kSQDNv/rasenggan.jpg','https://image.ibb.co/ciV2FF/rasenggan_prev.jpg'],
            'savage':['https://image.ibb.co/egn4Ua/savage.jpg','https://image.ibb.co/bDPUvF/savage_Copy.jpg'],
            'sepi':['https://image.ibb.co/k8CShv/sepi.jpg','https://image.ibb.co/hp802v/sepi_prev.jpg'],
            'weewoo':['https://image.ibb.co/jmejUa/weewoo.jpg','https://image.ibb.co/hrStNv/weewoo_prev.jpg'],
            'yamete':['https://image.ibb.co/fMADNv/yamete.jpg','https://image.ibb.co/fMADNv/yamete.jpg'],
            'otak dengkul':['https://image.ibb.co/dngEUa/otakdengkul.jpg','https://image.ibb.co/kuEUvF/otakdengkul_prev.jpg'],
            'whoa':['https://image.ibb.co/ffjQnv/whoa.jpg','https://image.ibb.co/ci2ZfF/whoa_prev.jpg'],
            'agak lucu':['https://image.ibb.co/d8vgSv/agaklucu.jpg','https://image.ibb.co/nECT7v/agaklucu_prev.jpg'],
            'ajglo':['https://image.ibb.co/nAagSv/ajglo.jpg','https://image.ibb.co/g8YeEa/ajglo_prev.jpg'],
            'asyique':['https://image.ibb.co/f8fsZa/asyique.jpg','https://image.ibb.co/bY9VLF/asyique_prev.jpg'],
            'bisa jadi':['https://image.ibb.co/kq4KEa/bisajadi.jpg','https://image.ibb.co/bV4KEa/bisajadi_prev.jpg'],
            'cengjed':['https://image.ibb.co/jfwzEa/cengjedface.jpg','https://image.ibb.co/bNfgSv/cengjedface_prev.jpg'],
            'dude what':['https://image.ibb.co/jsMMSv/dude_what.jpg','https://image.ibb.co/bYKmua/dude_what_prev.jpg'],
            'gay':['https://image.ibb.co/idHvnv/gaaayy.jpg','https://image.ibb.co/dHUmua/gaaayy_prev.jpg'],
            'gajah':['https://image.ibb.co/g0HH0F/gajah.jpg','https://image.ibb.co/kXyCZa/gajah_prev.jpg'],
            'fvkc':['https://image.ibb.co/c3Ux0F/go_fvck.jpg','https://image.ibb.co/dG1o7v/go_fvck_prev.jpg'],
            'god why':['https://image.ibb.co/hbrXZa/god_why.jpg','https://image.ibb.co/jwHT7v/god_why_prev.jpg'],
            'harimau':['https://image.ibb.co/jTwc0F/harimau.jpg','https://image.ibb.co/nfxNZa/harimau_prev.jpg'],
            'keep digging':['https://image.ibb.co/dEn0LF/keep_digging.jpg','https://image.ibb.co/e8Z2Za/keep_digging_prev.jpg'],
            'lapor polisi':['https://image.ibb.co/fDcd7v/laporpolisi.jpg','https://image.ibb.co/gVXZfF/laporpolisi_prev.jpg'],
            'mancing':['https://image.ibb.co/cv9Qnv/mancing.jpg','https://image.ibb.co/h32d7v/mancing_prev.jpg'],
            'mantan':['https://image.ibb.co/ko92Za/mantan.jpg','https://image.ibb.co/bT92Za/mantan_prev.jpg'],
            'missing':['https://image.ibb.co/mWmS0F/missing.jpg','https://image.ibb.co/fswufF/missing_prev.jpg'],
            'nobody cares':['https://image.ibb.co/fthBSv/nobodycares.jpg','https://image.ibb.co/buHd7v/nobodycares_prev.jpg'],
            'penampakan':['https://image.ibb.co/fZbufF/penampakan.jpg','https://image.ibb.co/caALLF/penampakan_prev.jpg'],
            'sadpepe':['https://image.ibb.co/cs9rSv/sadpepe.jpg','https://image.ibb.co/hx0WSv/sadpepe_prev.jpg'],
            'sultan':['https://image.ibb.co/iDPrSv/sultan.jpg','https://image.ibb.co/mL7ZfF/sultan_prev.jpg'],
            'tercyduk':['https://image.ibb.co/isZrSv/tercyduk.jpg','https://image.ibb.co/jfPEfF/tercyduk_prev.jpg'],
            'thumb up':['https://image.ibb.co/n3Qn0F/thumbup.jpg','https://image.ibb.co/dhSNZa/thumbup_prev.jpg'],
            'tydac mendydyc':['https://image.ibb.co/e7AJqF/tydacmendydyc_prev.jpg','https://image.ibb.co/mqxyqF/tydacmendydyc.jpg'],
            'mock':['https://image.ibb.co/ni29xv/mock.jpg','https://image.ibb.co/kuENHv/mock_prev.jpg'],
            'heuheu':['https://image.ibb.co/nJHRcv/heuheu.jpg','https://image.ibb.co/j6EHja/heuheu_prev.jpg'],
            'cogan':['https://image.ibb.co/dKxn2v/cogan_prev.jpg','https://image.ibb.co/dbawvF/cogan.jpg'],
            'perhaps':['https://image.ibb.co/jB2YqF/perhaps.jpg','https://image.ibb.co/hSi0LF/perhaps_prev.jpg'],
            'dude what':['https://image.ibb.co/gtcEEa/dude_what.jpg','https://image.ibb.co/gGrD7v/dude_what_prev.jpg'],
            #'':['',''],
           }
f = open('statics/gombal.txt', 'r')
list_gombal = (f.read()).splitlines()
f.close()
altia_url_tag ={'tertangkap basah':['https://image.ibb.co/neFJqF/tertangkap_basah_prev.jpg','https://image.ibb.co/nLEdqF/tertangkapbasah.jpg'],
                'bb++':['https://image.ibb.co/gYWwSv/bb.jpg','https://image.ibb.co/cAPuEa/bb_prev.jpg'],
                'deal with it':['https://image.ibb.co/dqWKfF/dealwithit.jpg','https://image.ibb.co/kg1wSv/dealwithit_prev.jpg'],
                'diem lu':['https://image.ibb.co/iZtAnv/diemlu.jpg','https://image.ibb.co/gMAC0F/diemlu_prev.jpg'],
                'ehe':['https://image.ibb.co/hnUN0F/ehe.jpg','https://image.ibb.co/bRjpfF/ehe_prev.jpg'],
                'fokyeah':['https://image.ibb.co/cnL6Sv/fokyeah.jpg','https://image.ibb.co/irmfnv/fokyeah_prev.jpg'],
                'hoam':['https://image.ibb.co/iGDRSv/hoam.jpg','https://image.ibb.co/bDO4Ea/hoam_prev.jpg'],
                'kata pak haji':['https://image.ibb.co/bVRD7v/katapakhaji.jpg','https://image.ibb.co/h30vLF/katapakhaji_prev.jpg'],
                'kelereng kuy':['https://image.ibb.co/ftbrua/kelerengkuy.jpg','https://image.ibb.co/drg20F/kelerengkuy_prev.jpg'],
                'leh uga u':['https://image.ibb.co/nhKBua/lehuga.jpg','https://image.ibb.co/mqr20F/lehuga_prev.jpg'],
                'mantep':['https://image.ibb.co/hFMfnv/mantep.jpg','https://image.ibb.co/gboRSv/mantep_prev.jpg'],
                'mantepv2':['https://image.ibb.co/gPiRSv/mantepv2.jpg','https://image.ibb.co/nJppfF/mantepv2_prev.jpg'],
                'mantepv3':['https://image.ibb.co/noZBua/mantepv3.jpg','https://image.ibb.co/fcEY7v/mantepv3_prev.jpg'],
                'mavok':['https://image.ibb.co/bYqjEa/mavok.jpg','https://image.ibb.co/cLupfF/mavok_prev.jpg'],
                'metbobo':['https://image.ibb.co/cqoFLF/metbobo.jpg','https://image.ibb.co/c60UfF/metbobo_prev.jpg'],
                'peace':['https://image.ibb.co/giqjEa/peace.jpg','https://image.ibb.co/hXcWua/peace_prev.jpg'],
                'sini sama om':['https://image.ibb.co/m8SmSv/sinisamaom.jpg','https://image.ibb.co/ipSxZa/sinisamaom_prev.jpg'],
                'slenderman':['https://image.ibb.co/g2CmSv/slenderman.jpg','https://image.ibb.co/hL8h0F/slenderman_prev.jpg'],
                'star wars':['https://image.ibb.co/fHSaLF/starwars.jpg','https://image.ibb.co/ePC9fF/starwars_prev.jpg'],
                'tercengang':['https://image.ibb.co/nAF6Sv/tercengang.jpg','https://image.ibb.co/k5F6Sv/tercengang_prev.jpg'],
                'tersyakiti':['https://image.ibb.co/jbpN0F/tersyakiti.jpg','https://image.ibb.co/gJhLnv/tersyakiti_prev.jpg'],
                'altia':['https://image.ibb.co/hnGKxv/altia.jpg','https://image.ibb.co/d2tA4a/altia_prev.jpg'],
                'berak kuy':['https://image.ibb.co/m3SgAF/berak_kuy.jpg','https://image.ibb.co/j1kZVF/berakkuy_prev.jpg'],
                'berak kuy v2':['https://image.ibb.co/hOmxja/berakkuyv2.jpg','https://image.ibb.co/eJM8qF/berakkuyv2_prev.jpg'],
                'minang bae':['https://image.ibb.co/nBe6cv/minangbae.jpg','https://image.ibb.co/kB8oqF/minangbae_prev.jpg'],
                'miwon':['https://image.ibb.co/nfssHv/miwon.jpg','https://image.ibb.co/jqCnja/miwon_prev.jpg'],
                'mwhehe':['https://image.ibb.co/g4J4VF/mwhehe.jpg','https://image.ibb.co/bSJhHv/mwhehe_prev.jpg'],
                'sini tak cium':['https://image.ibb.co/nA2WAF/sinitakcium.jpg','https://image.ibb.co/k52WAF/sinitakcium_prev.jpg'],
                'sultan payet':['https://image.ibb.co/jqGPVF/sultanpayet.jpg','https://image.ibb.co/jsp04a/sultanpayet_prev.jpg'],
                'swag':['https://image.ibb.co/dUH9xv/swag.jpg','https://image.ibb.co/nq3Sja/swag_prev.jpg'],
                'tarjan':['https://image.ibb.co/bKt4VF/tarjan.jpg','https://image.ibb.co/k6tSja/tarjan_prev.jpg'],
                'tercydukv2':['https://image.ibb.co/eABrAF/tercydukv2.jpg','https://image.ibb.co/nBy4VF/tercydukv2_prev.jpg'],
                 #'':['',''],
                 }
jawaban_bolehkah = ['boleh', 'ngga boleh', 'Ga tau', 'boleh ngettzz', 'boleh banget qaqa', 'G']
search_option = {'-g':'https://www.google.co.id/search?q=',
                '-s':'https://stackoverflow.com/search?q=',
                '-d':'https://duckduckgo.com/?q=',
                }
