from enum import Enum, unique


class EthereumNetworkNotSupported(Exception):
    pass


@unique
class EthereumNetwork(Enum):
    """
    Use https://chainlist.org/ as a reference
    """

    UNKNOWN = -1
    OLYMPIC = 0
    MAINNET = 1
    ROPSTEN = 3
    RINKEBY = 4
    GOERLI = 5
    ETC_KOTTI = 6
    TCH = 7
    UBQ = 8
    OPTIMISTIC = 10
    META = 11
    META_TESTNET = 12
    DIODE_TESTNET = 13
    FLR_FLARE = 14
    DIODE = 15
    FLR_COSTON = 16
    TCH_THAIFI = 17
    TST_TESTNET = 18
    SGB_SONGBIRD = 19
    BOBA_RINKEBY = 28
    RSK = 30
    RSK_TESTNET = 31
    GOOD_TESTNET = 32
    GOOD = 33
    TBWG = 35
    VAL = 38
    TLOS = 40
    TLOS_TESTNET = 41
    KOVAN = 42
    PANGOLIN_FREE_TESTNET = 43
    CRAB_CRAB_NETWORK = 44
    XDC = 50
    TXDC_TESTNET = 51
    CSC = 52
    CSC_TESTNET = 53
    BINANCE = 56
    SYS = 57
    ONTOLOGY = 58
    EOS = 59
    GO = 60
    ELLA = 64
    OKEXCHAIN_TESTNET = 65
    OKEXCHAIN = 66
    DBM_TESTNET = 67
    SOTER = 68
    MIX = 76
    POA_SOKOL = 77
    PC = 78
    GENECHAIN = 80
    METER = 82
    GTTEST_TESTNET = 85
    GT = 86
    TOMO = 88
    EOS_TESTNET = 95
    BSC_CHAPEL = 97
    POA_CORE = 99
    XDAI = 100
    WEB3GAMES_TESTNET = 102
    TT = 108
    XPR_TESTNET = 110
    ETL = 111
    FUSE_MAINNET = 122
    FUSE_SPARK = 123
    DWU = 124
    FETH_FACTORY127 = 127
    HECO = 128
    MATIC = 137
    DAX = 142
    PHT_SIRIUS = 162
    PHT = 163
    RESIL_TESTNET = 172
    AOX_XDAI = 200
    ENERGY_WEB_CHAIN = 246
    FANTOM = 250
    HECO_TESTNET = 256
    HPB = 269
    BOBA = 288
    KCC_TESTNET = 322
    THETA = 361
    THETA_TESTNET_SAPPHIRE = 363
    THETA_TESTNET_AMBER = 364
    THETA_TESTNET = 365
    CRO = 385
    RUPX = 499
    TAO_CORE = 558
    METIS_TESTNET = 588
    MACA_TESTNET = 595
    KAR = 686
    FETH_FACTORY127_TESTNET = 721
    CHEAPETH_CHEAPNET = 777
    ACA = 787
    HAIC = 803
    WAN = 888
    YETI = 977
    WAN_TESTNET = 999
    KLAY_BAOBAB = 1001
    NEW_TESTNET = 1007
    EVC_EVRICE = 1010
    NEW = 1012
    SAKURA = 1022
    CLOVER_TESTNET = 1023
    CLOVER = 1024
    METIS = 1088
    MATH = 1139
    MATH_TESTNET = 1140
    MOON_MOONBEAM = 1284
    MOON_MOONRIVER = 1285
    MOON_MOONROCK = 1286
    MOON_MOONBASE = 1287
    MOON_MOONSHADOW = 1288
    GANACHE = 1337
    CATECHAIN = 1618
    EGEM = 1987
    EDG = 2021
    EDG_BERESHEET = 2022
    KORTHO = 2559
    FANTOM_TESTNET = 4002
    IOTEX_IO = 4689
    IOTEX_IO_TESTNET = 4690
    ESN = 5197
    SYS_TESTNET = 5700
    ONTOLOGY_TESTNET = 5851
    RBD = 5869
    SHYFT = 7341
    MDGL_TESTNET = 8029
    GENECHAIN_ADENINE = 8080
    KLAY_CYPRESS = 8217
    KORTHO_TEST = 8285
    OLO = 8723
    OLO_TESTNET = 8724
    BLOXBERG = 8995
    SMARTBCH = 10000
    SMARTBCHTEST_TESTNET = 10001
    GEN = 10101
    SHYFT_TESTNET = 11437
    MTT = 16000
    MTTTEST_DEVNET = 16001
    GO_TESTNET = 31337
    FSN = 32659
    NRG = 39797
    ARBITRUM = 42161
    CELO = 42220
    ATH_ATHEREUM = 43110
    AVALANCHE = 43114
    CELO_ALFAJORES = 44787
    NRG_TESTNET = 49797
    CELO_BAKLAVA = 62320
    VOLTA = 73799
    AKA = 200625
    ARTIS_SIGMA1 = 246529
    ARTIS_TAU1 = 246785
    SPARTA_TESTNET = 333888
    OLYMPUS = 333999
    ARBITRUM_TESTNET = 421611
    ETHO = 1313114
    XERO = 1313500
    MUSIC = 7762959
    MUMBAI = 80001
    PEP_TESTNET = 13371337
    ILT = 18289463
    QKI = 20181205
    AUX = 28945486
    JOYS = 35855456
    AQUA = 61717561
    TOYS_TESTNET = 99415706
    OLT = 311752642
    IPOS = 1122334455
    AURORA = 1313161554
    AURORA_TESTNET = 1313161555
    AURORA_BETANET = 1313161556
    PIRL = 3125659152
    OLT_TESTNET = 4216137055
    PALM_TESTNET = 11297108099
    PALM = 11297108109
    GATHER_DEVNET = 486217935
    GATHER_TESTNET = 356256156
    GATHER_MAINNET = 192837465
    EVMOS_TESTNET = 9000
    EVMOS_MAINNET = 9001

    @classmethod
    def _missing_(cls, value):
        return cls.UNKNOWN
