import pytest
import hashlib


def num_sequences(n: int) -> int:
    ''' 
    Returns the number of different sequences of steps to cover n units.

    Each step can cover 1 or 2 units.

    Parameters:
    - n : the number of units to cover.

    Constraints:
    - 1 <= n <= 2 * 10**4

    Return:
    the number of different sequences of steps to cover n units.
    '''
    a, b = 1, 2
    while n > 1:
        a, b = b, a + b
        n -= 1
    return a


data = [
    (7968, 'e8ce3f33d5358c467e47ab264f10df61125fdbda7d3b9ad56de4ed2d82b9d2e4'),
    (15352,
     '962de5d18533c0eb13535139873e47cab3c03eb5dbe345ef936d1e0752aa6170'),
    (12573,
     'dc0eaf0bed837834778a0a0fc1a6d2c2d62be8fddaca0e58ff628b2b0529a6cd'),
    (18091,
     '5bfd21227d945ac4a42a3fd8e36356b9b34ba57f9283a0cbf24a79c979ee1180'),
    (15453,
     'e547721c5e7fd8e002fd9ed640c9720a37510eb878304ec87ecc423e481f6c27'),
    (18282,
     '67608976a9bd4cd2e3355d802f4d569e96cb465d1d504cad63d82437d61a2d08'),
    (7453, 'c76f06251a053e81c9070e37885481b16814fbd529f5d52c7c877858bd7a7ee2'),
    (14815,
     '5dbf8149baba7f80580f4db599976560e1a10c2c112b43297ac441274c9da12c'),
    (17468,
     '3479dbfe00847d5bc7236d32ff1d7f050b4bff09709247f66e17f63f402e3598'),
    (2849, '8a54e540103d05df6284f3eb105444d94a7a80846ed62ded8da21a432d7a213e'),
    (18382,
     'd25ff15cedb7143d8bdb57d65021d177fc39af8b3f5dd463d0f0a6302d7009a0'),
    (9040, '9bf0dfa08452b901343bf12bcb942f168714b941f7828160d7c0c11f11e101db'),
    (16986,
     '27f164bff4cf149bcaba4596bc99e9c4c3db69fb721fdf6e7cd5ee57be0b75a4'),
    (14736,
     '2bab4d5261b04b118b349723aa985e4974777b59c596a815b2efc5cc7d02d2d6'),
    (10151,
     '2cb9e9a44a7cf0220839d092f084e2d38ac9597d5cf7effd1e319a87647a9e9f'),
    (2144, 'f8a72f533760c9e4d0b50be6596ca5e017484542213423110e480f47195e242b'),
    (6728, '9a2d30860ae9edb76dd9e1508ed493ca6346b768f022aff8fff8448f91bb9e03'),
    (5517, 'f821e0d12ac05128fa14fc2818895fb9dac9be6956ee50f227d0313c7a30038a'),
    (17168,
     'a85b22815550b5bc4a7c204901901feff0772ecd80a9e0c74ff38e915196408d'),
    (15625,
     '8cafb857898db47acae03d48772ed54fdf6b8c1856cc972f0324feee3a6914b0'),
    (4103, '1c5aeb8e25f4edb9999bf4a2e9a44666f63b8f67d1f630480179a52eab3db9a5'),
    (11861,
     'adba278d21738a1f5bcb61bdf8fa9591ce74346d20e6d3adccfa5470c294d90c'),
    (17355,
     '095163c87d7c4b34c3ae8f0d937952adf5ffdd38787feb59d14a1c2a63d9fa5f'),
    (8257, '96d74cce999b656062af7195152b87ea6eb9e430c07aa94a6ea7630d7db38acb'),
    (3959, '68a2152951a866fef039175610ee17c02529bd6db9cc099b54d983b3788285d9'),
    (3000, '84b349c45cfc216fdadbc946066b3f1c0a5066c2704ed5b270a904eba51f1b6f'),
    (1377, '051e61cb31ffac80610d1a123fe8143200325d318a426a3b030e8a1fe734a016'),
    (18859,
     '8aee2c209f22b460b90436edb38e4d6c3d21e51886ef3cc712daf48a17e5addd'),
    (2378, 'ba350642bda47c8c96472c76c159580d9c3a7a0b602c619654dc13769b692a2e'),
    (428, 'b6293251de21845268a978c4a152c3c354fcfe66c7aee076b8968b9ad96b7678'),
    (5755, '04a63657688ce57cc423f53c825803f049d3a3f43090bc00f528df2ea49d4c3d'),
    (14110,
     '792be7f236fbc6b0f9176d482af17d8d7e85fdb7cfb678c4c85bf2579e3153fc'),
    (3523, '04d859ab5164eaa646fbdaad527bbbde594b2bdb1602030bafc558c65d8d9f63'),
    (6994, 'e3c6926c09d807b9a7d769e365d9e2b2a38ef910ec243d52c0b54ff04c111cf3'),
    (11959,
     '8090b09dbe060adadf891b3188914a503c0a5415e579111086b95c0256e21a17'),
    (4983, '5e884ee4b6d5d56e552d60db814ebbce757f270a2cefb5733d9050a9b5da1d0d'),
    (414, 'eae54265ce3642108997400aeeca1b7a40c234654b8c3fcd5df21f6860446aba'),
    (2324, 'aa84b2fdca6825a51ad4044e06f2db642145c3d5a0bdecd2c7fe43e661a02c3b'),
    (14149,
     '96e6377de6b738e4984f0d125b39d77ca2525a23a84e33174625bd36a410b60d'),
    (1383, '540be5bb8c9cad705797299a3c8cf65f92a9ddc74129c65f7165a44a795d768e'),
    (16975,
     '0554572a4ecc0531cbab5df48bab511059ac97b6e1dfde4d6281c4340e765108'),
    (3114, 'aa306d0f8b072616988113eb41d8ddf762800c273ed26f47eafcf58be78c4ad6'),
    (6771, '7b6cf5a1877aef3b36db71bb670260c00b7fd27c481e81897c98a19334daefa9'),
    (9622, 'dd12480f0859bb280ed44c0ee6a1dd945df80451f48086724c1380a7eb44005f'),
    (4377, '73690b3d60fd4d718cbfaf8a6fa65ede1b5fb8104eb6231c15d6717fdbcf658f'),
    (19278,
     '1db3cd311eb42305a9e8ae5e476682814bdcbcc46de96a77fcd810c2a17532b7'),
    (6501, '971a3bb11fe7bdf2638a100fd7565254a5daba58794bed9a0416521a2e8d3f33'),
    (5032, '871b1c90dfc5d6cbb6bad291b56bca5a3d9246b96fe427c6d1ebcd8143258a9d'),
    (10492,
     '65765c47b58981d21179bba46f9fbe840aaea4071ef8b364449168656d033fbf'),
    (306, '14a20697c627feed8cbaffabd1faa2c02ba9995add9f48d920ce8945582e5da8'),
    (9492, '1ad608d0f306c9d626bff804f82857bafcd83f0230dfe063163b39c4096cd166'),
    (2662, '16a4b7e1c4c6e82dd19f2095d47311c3318be2a2add4dbd853bf72754e820ff8'),
    (18009,
     'b86960ab428efa113271a1c3a27fd2f1d5707cf162e0c5cf7d1841264e75a410'),
    (16666,
     'dcc7777fe296bfcd642b7973bda90a59573ea72bf5bca30257e539d427574f86'),
    (7650, 'cb3d4e0d7d5ca44c75cfe779520a77963f0c671ac2cc978bccfb538a6dd2439c'),
    (17269,
     '8d649670dc34aca88e8c6e147a053cc865713c23c847a53d436896078c28c9e1'),
    (1524, 'b9329e03e43bab083219f96cdb812b94317bc3ea6f8176f214ad8f4139f202b8'),
    (3773, 'd7ab245103634257c2943e50cc78dfd231b6c85a88f9a8afcb9e80d5c8f3575e'),
    (13678,
     '86d1204a22b434b8e94336d0f54ff627770e88de84e5649322812d4df3cca211'),
    (4045, '562700bd35d46b8902daf46babc0e2b4db984c01dc55fa54afd649ea22e70f35'),
    (4363, '72d2cc7e83b3efe0bc42d482e55fbcb4a26a93a64c5aa025ea5797b55b8fc49a'),
    (12267,
     'a931bc22cc64f42d85d24d647ad5884fe7d7bfcfe4470d3a8b784356d378d5bb'),
    (7471, '4a4e0aee0f6c27bea7b2ce47362f78a4a24707c365500285c6c5a8d0702cd516'),
    (10568,
     '092249232b453b9bb95561f94f8cb1f8cc5b1f75f7289c1ad63f1abe70299de5'),
    (3946, '9ffda6176c76ab4d2c76c3f7879bf6f342192132c38a9a61f4a0b10a9b4d05fe'),
    (10791,
     '6bde46fce928067a6381928427df749a6f5442225ae3dae325d4ab6efdceeab9'),
    (18751,
     '760896c0e38f0a7fb01ea01808d5c52cb65503a2c232351cc43cc4de4e076655'),
    (534, '024492d3e3d0158b13b928090ac926cc05f6c7a550e0b13e74d82ef0559b43aa'),
    (4018, '51062159a9325e676dcf822b1c15eecaab6c5780cb1c318e381e83e13dd18d00'),
    (866, '07c612afcc0a9a3731e645406c46b56034f4b308f2231d52fae0999ac740f347'),
    (13748,
     '7e9e188d2e0ab87d307b534c3f4a707a229ba1461a00cdce5f39a47bf622d5e9'),
    (15009,
     '789172d7945652edb2bee137b1908cd017a2b3fe3904b16b5b4e85f31317dd5f'),
    (4010, '48574fb23c7aac933132918bec9017ebf8cc1ebc282fae1402df14ef3bf7babc'),
    (11787,
     '15555e66ff54049ab3ccd8565ffd35f424c470b8af490f133bf0238e0a6a2e5c'),
    (14745,
     '2f8bc747b4657986d2d9a30aba6fa08871c241d969dc6c1bceda6e334de99ced'),
    (9507, '00a9eb538c4148c975a3e8fa85d22f61b621cccf8a26ba1776c9c9de447528fd'),
    (14652,
     '33b29ffbeafb407d652d6542a5b48d5b0e3c77113d4ee3320258d67b88225e00'),
    (11111,
     'f036427bb2cfd9233316aca766a9bd67ce2110af918cfbb45e3f7a08ab4d7ee6'),
    (2798, '7387422c076303a81a5241a1cbedc5d5432d0a5517fa096905578ee70fd6ce05'),
    (4803, 'aaa149e25e532e48fa11dddc9d166d6d3ef332c56177b3664861846f93c1d98a'),
    (9848, 'a1e12898e1cd89e6b0a52ca68d1ab03b5898bb98ba0cc6c7184fd7d6a94c7cac'),
    (926, '28449ecf19924fdbd870b60ee3c222873195bf2a0fe17c2e22573229d7e3b7e5'),
    (13062,
     '7ed3481f0b30d3ab2da7e95e8353d0b4c24609c4fc729222135d6ada35b19a8b'),
    (5474, '76d735c61db0f90698f27a7ef1d6c37d37a84848ea8f7bc82b24070c875ea171'),
    (4111, '5c6058e03eb6f98fd71d9dc2898f3a796a6a8c8a20e665cd4d4245fecc8cc787'),
    (19616,
     '87ed92d312feb734c727096b6467e6713d8e9fef125a8f3b6d2c15ffde71d203'),
    (18589,
     '9ed62103fff1438c309dee87f6a310088bd67e6b02ca8ad75fee10928e551ab8'),
    (15705,
     '8d214d9faa711d5108e947b17ca5505a56c7f3b8b5ac355e5c5b00587782aacc'),
    (10352,
     '13e266437fdb989bb5d941831a31fe038f0bbf9b70d34e757a963ca9db6994c9'),
    (3800, 'f7f267555800f86be119faaf3dcad95224ca5a55494b3596fb35ef03df2fb5be'),
    (8330, '60c28fdd5e84f639c02112447a187f39f6515ca899f4932ed2f9dcf1a42dc575'),
    (19495,
     '6a474342e2fb7140dcd575d485e5841dbb5cb8abb957205b2466508e8bf8fe29'),
    (2373, 'cc29f6cd02586d5bb15bafc97244f5c6b05440d548c424248186971445eeaa5e'),
    (13336,
     '354f4b87bbc0a11dc0cec68a2eab1214ae450a89c21a0a41592cb5a3dc0ffa53'),
    (19307,
     'bddab29ce0c9af2be6cbfb052acda4bd5b3008a14db2aea307f8a4d31cb0cf51'),
    (19062,
     '5d59f0e046a2f8d351c2a619bec0e6e37e0b159ad7b9f11ba59632a12ad49e68'),
    (10819,
     '2ccc171789ca0c0467b50afc9ec7736ddeec48408d5848ce85a57035709ce88d'),
    (2022, '915e9df4dd7881a114e3956e16325d398078a68bfde8d5adb488e9d82f0a3549'),
    (1453, '895353a54b98615c3f05f74546534bb04ba56db6c400ee9971c96261ecfdee16'),
    (11793, '907bd20b801b756be40a574abf5bc9404e6a788b8bd8494fb94231b54aa842c2')
]


def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()


@pytest.mark.parametrize("n, out", data)
def test_sequences(n, out):
    assert hashcode(num_sequences(n)) == out


if __name__ == "__main__":
    pytest.main()