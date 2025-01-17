"""
 AUTHOR: Diego Salas Noain/Diane Renard
 FILENAME: constants.py
 SPECIFICATION: We need to send an HTTP request with a header so we don't get categorized as a webscrapping bot
 FOR: CS 5364 Information Retrieval Section 001
"""

headers = {
  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
  "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
  "accept-language": "en-US;en;q=0.9",
  "accept-encoding": "gzip, deflate, br"
}

headers_product_detail = {
  'authority': 'www.walmart.com',
  'accept': 'application/json',
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/json',
  'cookie': 'wmtboid=1664549930-5126369994-17451472320-54535851; _pxhd=d185f1f1633b54d28bbd49e599df7149efafa0c20f19a44da9107360bd18be27:64cd1f46-40d0-11ed-9e67-754248526b58; bm_mi=FF061A8D06DE9A072D559BDE5BAE4205~YAAQtfAPF6/5PV6DAQAAeEfojhHK3BOvaSV3KACqTKjdYlscvjR0uxkHdRquac7mR1RatomxkCmIsY/FrwZdQnlpg//R/EfewpJkqud7g6ctSY9wLxUWxNsPeMdA6VrbqNYb+KEowomy9IuzBFvRV+4+G+G8+MTJmk5nFE1ojCMWwv5MEMZEBGVpS0X+cM9W6LQ716ylFWOoxIyCvW6ipm4sw3iJoDTirFpcmFM0O50SnPP0lUvpnmrWkVW90ujsJqey9W1X11AO5zVRO7Odp8h+ofXxcfTE3DGWSxVGyQspViqvzP9u4/J8qaH4kIfOgmgLRyuW~1; pxcts=6566baaf-40d0-11ed-99d9-494f706f574f; _pxvid=64cd1f46-40d0-11ed-9e67-754248526b58; _pxff_rf=1; _pxff_fp=1; _pxff_cfp=1; ak_bmsc=427BD4124F5F7FD1D770CEA3B3E39E3E~000000000000000000000000000000~YAAQcVgyuOzG3X2DAQAA+HrojhFpoiTroFA42QG/jn1Puns4ZmExS43klJgsIYmL918S7xhdkzzfSnr5agImlKYv/tDWXJHyKu9CqnWFB3Iyni+t9B4V0QkkmU/lT/06PwtFVHCkpLU10Lsc5kl8K10gbie5KfXgNlsr1rXi9dYplVLA5w4UjJEgjPjzwZrOoyQyjpGMRD2l73a2aQsYG2m5YlEy5/6BC8JCbp3LIc1KzawfYu2YfC4Ma8Bj1E0IwOTelcoTDlNXqvkSpjBqu/DQVOh7lbg6Rm6NgGbPIlsaSt3zalEkwWMrtqDyyvzGTyiZ1e/MpttffKtt4E80na472uo8YaxptWw77M7+3BcU3Ofei8ZtalDyfzXuBVe1/Gv+D4nDHQD2m8LgoMvPPpqewLn12Fkx6G5wcnpJQDUnZ3zcWW8=; auth=MTAyOTYyMDE4m%2FS3ADENErTLDSZuFykzoLAFFXmO4h2OgTMTvJhVENhrCQGLIlcueveWMpBq2bCQHR5nTn5l2i9aH3Bvp9CuNqX7vjHgvLAOGi7%2FTbZYo27zIQiMBXjCsRCbgt3249Dg767wuZloTfhm7Wk2Kcjygv3M5Jnvc7ePkiG6%2BkglNAA48hgC7M94GN8JFWJnvQFKNcuNdRO2Ij5Z3w5BhcIlaXjLGDVB1Zk6Ya%2BdennMpvEUMk70P8glgOEpLOprhDfMM%2FFHGZ2dCNmxWrdkwqEKroVsQJaQrIZmbmgA6Jq%2FE0mPKrdOtWYfxmamQUPic2awBqIU9vssWLJSP6sgqkMkm2QC%2FxrFWd7g%2F3%2F4tt1LYHOv1atMyHqtKwZtSPwsxsUM0QwFsHetUXdQUwCmzRlyakjyrOXbKKhH072NS%2FW0j%2FU%3D; ACID=28b69912-4443-47bc-b2f0-a83138e45cba; hasACID=true; assortmentStoreId=5435; hasLocData=1; TB_Latency_Tracker_100=1; TB_Navigation_Preload_01=1; TB_SFOU-100=; vtc=SHHyvlpshEimQt03lKVACM; bstc=SHHyvlpshEimQt03lKVACM; mobileweb=0; xpth=x-o-mverified%2Bfalse; xpa=-F4Tj|20yr2|2SWkj|4-FVr|5aZhw|5ccTK|5q86Y|6r4vW|9T1D1|9e61f|BrNRv|CShcr|CVef3|DJvKV|EyvKe|FtGKq|Fxy8_|GcXzr|GkqrP|H9VcM|Jvjjj|K2IBM|MJuLK|MQ6mX|NBAls|Nnski|RAUB0|RWwzc|Sf0l7|Twnv9|Tz5n8|UZlgh|Uq_L_|V-nnO|WrDbE|X57A7|XA7Ad|Y9_n0|ZgMny|a0tqZ|bj38K|buiiw|cL8HI|ccDGr|dth3N|ebwX-|gVG-b|lNat-|mM0Sa|mk3nQ|qQczS|riTZF|rlJqf|tWk_I|tzVuW|u8ztl|vuySs|wWXeG|xOe2Z|xyycY|yK_ny|zFeZ5|ziyTH; exp-ck=20yr212SWkj19e61f1CVef31DJvKV1FtGKq1Fxy8_1GcXzr1Jvjjj1K2IBM1MJuLK1MQ6mX1NBAls1Nnski1RAUB01RWwzc3Sf0l71UZlgh1V-nnO1X57A71XA7Ad2a0tqZ1bj38K1cL8HI1ccDGr1dth3N1gVG-b1mM0Sa1mk3nQ2qQczS1tWk_I1u8ztl1vuySs1wWXeG1xyycY1yK_ny4zFeZ51ziyTH1; xpkdw=1; locDataV3=eyJpc0RlZmF1bHRlZCI6ZmFsc2UsImlzRXhwbGljaXQiOmZhbHNlLCJpbnRlbnQiOiJTSElQUElORyIsInBpY2t1cCI6W3siYnVJZCI6IjAiLCJub2RlSWQiOiI1NDM1IiwiZGlzcGxheU5hbWUiOiJTYW4gSm9zZSBTdXBlcmNlbnRlciIsIm5vZGVUeXBlIjoiU1RPUkUiLCJhZGRyZXNzIjp7InBvc3RhbENvZGUiOiI5NTEyMiIsImFkZHJlc3NMaW5lMSI6Ijc3NyBTdG9yeSBSZCIsImNpdHkiOiJTYW4gSm9zZSIsInN0YXRlIjoiQ0EiLCJjb3VudHJ5IjoiVVMiLCJwb3N0YWxDb2RlOSI6Ijk1MTIyLTI2MjgifSwiZ2VvUG9pbnQiOnsibGF0aXR1ZGUiOjM3LjMzMDk5NCwibG9uZ2l0dWRlIjotMTIxLjg2MDQzMX0sImlzR2xhc3NFbmFibGVkIjp0cnVlLCJzY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJ1blNjaGVkdWxlZEVuYWJsZWQiOnRydWUsImh1Yk5vZGVJZCI6IjU0MzUiLCJzdG9yZUhycyI6IjA2OjAwLTIzOjAwIiwic3VwcG9ydGVkQWNjZXNzVHlwZXMiOlsiUElDS1VQX0JBS0VSWSIsIlBJQ0tVUF9DVVJCU0lERSIsIlBJQ0tVUF9JTlNUT1JFIiwiUElDS1VQX1NQRUNJQUxfRVZFTlQiXX1dLCJzaGlwcGluZ0FkZHJlc3MiOnsibGF0aXR1ZGUiOjM3LjM1MjIsImxvbmdpdHVkZSI6LTEyMS45NTgzLCJwb3N0YWxDb2RlIjoiOTUwNTIiLCJjaXR5IjoiU2FudGEgQ2xhcmEiLCJzdGF0ZSI6IkNBIiwiY291bnRyeUNvZGUiOiJVU0EiLCJnaWZ0QWRkcmVzcyI6ZmFsc2V9LCJhc3NvcnRtZW50Ijp7Im5vZGVJZCI6IjU0MzUiLCJkaXNwbGF5TmFtZSI6IlNhbiBKb3NlIFN1cGVyY2VudGVyIiwiYWNjZXNzUG9pbnRzIjpudWxsLCJzdXBwb3J0ZWRBY2Nlc3NUeXBlcyI6W10sImludGVudCI6IlBJQ0tVUCIsInNjaGVkdWxlRW5hYmxlZCI6ZmFsc2V9LCJkZWxpdmVyeSI6eyJidUlkIjoiMCIsIm5vZGVJZCI6IjU0MzUiLCJkaXNwbGF5TmFtZSI6IlNhbiBKb3NlIFN1cGVyY2VudGVyIiwibm9kZVR5cGUiOiJTVE9SRSIsImFkZHJlc3MiOnsicG9zdGFsQ29kZSI6Ijk1MTIyIiwiYWRkcmVzc0xpbmUxIjoiNzc3IFN0b3J5IFJkIiwiY2l0eSI6IlNhbiBKb3NlIiwic3RhdGUiOiJDQSIsImNvdW50cnkiOiJVUyIsInBvc3RhbENvZGU5IjoiOTUxMjItMjYyOCJ9LCJnZW9Qb2ludCI6eyJsYXRpdHVkZSI6MzcuMzMwOTk0LCJsb25naXR1ZGUiOi0xMjEuODYwNDMxfSwiaXNHbGFzc0VuYWJsZWQiOnRydWUsInNjaGVkdWxlZEVuYWJsZWQiOnRydWUsInVuU2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwiYWNjZXNzUG9pbnRzIjpbeyJhY2Nlc3NUeXBlIjoiREVMSVZFUllfQUREUkVTUyJ9XSwiaHViTm9kZUlkIjoiNTQzNSIsImlzRXhwcmVzc0RlbGl2ZXJ5T25seSI6ZmFsc2UsInN1cHBvcnRlZEFjY2Vzc1R5cGVzIjpbIkRFTElWRVJZX0FERFJFU1MiXX0sImluc3RvcmUiOmZhbHNlLCJyZWZyZXNoQXQiOjE2NjQ1NzE1OTY3MzUsInZhbGlkYXRlS2V5IjoicHJvZDp2MjoyOGI2OTkxMi00NDQzLTQ3YmMtYjJmMC1hODMxMzhlNDVjYmEifQ%3D%3D; locGuestData=eyJpbnRlbnQiOiJTSElQUElORyIsImlzRXhwbGljaXQiOmZhbHNlLCJzdG9yZUludGVudCI6IlBJQ0tVUCIsIm1lcmdlRmxhZyI6ZmFsc2UsImlzRGVmYXVsdGVkIjpmYWxzZSwic3RvcmVTZWxlY3Rpb25UeXBlIjoiTFNfU0VMRUNURUQiLCJwaWNrdXAiOnsibm9kZUlkIjoiNTQzNSIsInRpbWVzdGFtcCI6MTY2NDU0OTk5NjczMn0sInBvc3RhbENvZGUiOnsidGltZXN0YW1wIjoxNjY0NTQ5OTk2NzMyLCJiYXNlIjoiOTUwNTIifSwibXAiOltdLCJ2YWxpZGF0ZUtleSI6InByb2Q6djI6MjhiNjk5MTItNDQ0My00N2JjLWIyZjAtYTgzMTM4ZTQ1Y2JhIn0%3D; xptc=assortmentStoreId%2B5435; _astc=ed6facdfb5f05890796c95b900be7920; adblocked=false; TBV=7; xpm=1%2B1664549996%2BSHHyvlpshEimQt03lKVACM~%2B0; _px3=7a58cc65ba7864c4a86a9d656641aee59ad133a35a2d42420782d2f95289b805:exozdh1wqL5vfeEqvzNRPjK+07z+nrE0mG4nb68/HEbOi9jTonHu00Qtu3gpsmWUBKaOTzYOkekTdwwq3vA2BA==:1000:nHTfAdQculvfZFCOWhXIE0BSKqvindH7EMThQImDNi55lV7za0M5rBlBhPfzwTpWZJv50p4O1SeA8NTbVos9lMYCgObmx9ROtERA3eUFj3OJzS0Lk2SrHd6uU8FQUibnBkQ+GbsZOtzsMQg2TM+PIit84F8WJMIN4oW9JsCQdLpLvJp2hXCSIrctgIbMgjRBZpiMk0KqBYGaPU+Lb1XCNg==; xptwg=1249607512:74C91B407A06B8:12D563A:F0E03738:6A17E489:9146B528:; xptwj=cq:2d83382ea8b4008a6b4b:aSlTIp/RcJbS8HMfC5betxkbvr5uHZICheIsGW5bfwU+OPJAzVqRzCWZHHjgDWrBLwOidAYtaCrlTuxIf9LZLkTJBqqG+35jx1vccc+x4A1q7aqvlJNYlQ==; TS012768cf=01096c3e4c76fe7e3e5127b4d55f79499ead136a086b5afc277cc26374e004bf3193f00e83af1e4ee7cda673a3833971405e78e3b5; TS01a90220=01096c3e4c76fe7e3e5127b4d55f79499ead136a086b5afc277cc26374e004bf3193f00e83af1e4ee7cda673a3833971405e78e3b5; TS2a5e0c5c027=0818fc09caab2000c1affd2abf6f95e6060c67eed9eff6ff6c76412d338160570c4ed9bce0eb14ff08237fd51a113000ae4ed63842d75f4f90b7a3358414ae7a7c75796fc9e61eaaead3396440893b585f6fbea65d79dde8ba6202a37805c2ed; akavpau_p2=1664550616~id=fcafda7c301bb14fb19e71298df93109; bm_sv=04781699A3DF7EC1C8FE95BE14B11109~YAAQZlgyuKoBiG2DAQAA2ZTpjhGvajvPsDMc8iyvJd/OFMRW7qGJbPhXP/7UTo8xUUGNRg7ZZTsX+o7kIviMXlePwixp1erKXDWB0yP6KUI6L9bK7iE0DwlA3IgTgVIadlTh4aQ9Dvys18QrIJwnv+wm5A0dg4guFHLz0AVON9vdqNE7xjCqRfsyolxqP6ErPqXswSf9sqG7vyUTsCeFIX6FhUuUvngvd+wIuUExYMi2P1Cq6G8UCD9ygepQYeCInQA=~1; TB_SFOU-100=; com.wm.reflector="reflectorid:imp_xLCzEpzhSxyNRTVQiY0Eh0ZsUkDWsnwPNVIoQU0@lastupd:1664512285000@firstcreate:1663174987745"; vtc=Utds7xsWsBDI9xFRMqnn4U',
  'device_profile_ref_id': '2bJl3nEP2veHhmOB6NlQGA8EdP89IyOm9PLK',
  'origin': 'https://www.walmart.com',
  'referer': 'https://www.walmart.com/search?q=banana',
  'sec-ch-ua': '"Microsoft Edge";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'traceparent': '00-ffaa1f8f6e71e1af18ed38e141caa57d-6f58136eecdd93f6-00',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53',
  'wm_mp': 'true',
  'wm_page_url': 'https://www.walmart.com/search?q=banana',
  'wm_qos.correlation_id': 'OhSQQ4CIj3wL89dPmXf9LMPp4aQUuzc5oEED',
  'x-apollo-operation-name': 'SortAndFilter',
  'x-enable-server-timing': '1',
  'x-latency-trace': '1',
  'x-o-bu': 'WALMART-US',
  'x-o-ccm': 'server',
  'x-o-correlation-id': 'OhSQQ4CIj3wL89dPmXf9LMPp4aQUuzc5oEED',
  'x-o-gql-query': 'query SortAndFilter',
  'x-o-mart': 'B2C',
  'x-o-platform': 'rweb',
  'x-o-platform-version': 'main-1.23.0-4561b3',
  'x-o-segment': 'oaoh'
}


