from .adaptive import Adaptive
from .alternator import Alternator
from .ann import EvolvedANN, EvolvedANN5, EvolvedANNNoise05
from .apavlov import APavlov2006, APavlov2011
from .appeaser import Appeaser
from .averagecopier import AverageCopier, NiceAverageCopier
from .axelrod_first import (Davis, Feld, Grofman, Joss, Nydegger,
                            RevisedDowning, Shubik, SteinAndRapoport,
                            TidemanAndChieruzzi, Tullock, UnnamedStrategy)
from .axelrod_second import (Black, Borufsen, Cave, Champion, Colbert,
                             Eatherley, Getzler, Gladstein, GraaskampKatzen,
                             Harrington, Kluepfel, Leyvraz, Mikkelson,
                             MoreGrofman, MoreTidemanAndChieruzzi,
                             RichardHufford, Tester, Tranquilizer, Weiner,
                             White, WmAdams, Yamachi)
from .backstabber import BackStabber, DoubleCrosser
from .better_and_better import BetterAndBetter
from .bush_mosteller import BushMosteller
from .calculator import Calculator
from .cooperator import Cooperator, TrickyCooperator
from .cycler import (AntiCycler, Cycler, CyclerCCCCCD, CyclerCCCD,
                     CyclerCCCDCD, CyclerCCD, CyclerDC, CyclerDDC)
from .darwin import Darwin
from .dbs import DBS
from .defector import Defector, TrickyDefector
from .doubler import Doubler
from .finite_state_machines import (TF1, TF2, TF3, EvolvedFSM4, EvolvedFSM16,
                                    EvolvedFSM16Noise05, Fortress3, Fortress4,
                                    FSMPlayer, Predator, Pun1, Raider, Ripoff,
                                    SolutionB1, SolutionB5, Thumper)
from .forgiver import Forgiver, ForgivingTitForTat
from .gambler import (Gambler, PSOGambler1_1_1, PSOGambler2_2_2,
                      PSOGambler2_2_2_Noise05, PSOGamblerMem1, ZDMem2)
from .geller import Geller, GellerCooperator, GellerDefector
from .gobymajority import (GoByMajority, GoByMajority5, GoByMajority10,
                           GoByMajority20, GoByMajority40, HardGoByMajority,
                           HardGoByMajority5, HardGoByMajority10,
                           HardGoByMajority20, HardGoByMajority40)
from .gradualkiller import GradualKiller
from .grudger import (Aggravater, EasyGo, ForgetfulGrudger, GeneralSoftGrudger,
                      Grudger, GrudgerAlternator, OppositeGrudger, SoftGrudger)
from .grumpy import Grumpy
from .handshake import Handshake
from .hmm import EvolvedHMM5, HMMPlayer
from .human import Human
from .hunter import (AlternatorHunter, CooperatorHunter, CycleHunter,
                     DefectorHunter, EventualCycleHunter, MathConstantHunter,
                     RandomHunter)
from .inverse import Inverse
from .lookerup import (EvolvedLookerUp1_1_1, EvolvedLookerUp2_2_2, LookerUp,
                       Winner12, Winner21)
from .mathematicalconstants import Golden, Pi, e
from .memoryone import (GTFT, ALLCorALLD, FirmButFair, MemoryOnePlayer,
                        ReactivePlayer, SoftJoss, StochasticCooperator,
                        StochasticWSLS, WinShiftLoseStay, WinStayLoseShift)
from .memorytwo import AON2, MEM2, DelayedAON1, MemoryTwoPlayer
from .mindcontrol import MindBender, MindController, MindWarper
from .mindreader import MindReader, MirrorMindReader, ProtectedMindReader
from .mutual import Desperate, Hopeless, Willing
from .negation import Negation
from .oncebitten import (FoolMeForever, FoolMeOnce, ForgetfulFoolMeOnce,
                         OnceBitten)
from .prober import (CollectiveStrategy, HardProber, NaiveProber, Prober,
                     Prober2, Prober3, Prober4, RemorsefulProber)
from .punisher import (InversePunisher, LevelPunisher, Punisher,
                       TrickyLevelPunisher)
from .qlearner import (ArrogantQLearner, CautiousQLearner, HesitantQLearner,
                       RiskyQLearner)
from .rand import Random
from .resurrection import DoubleResurrection, Resurrection
from .retaliate import (LimitedRetaliate, LimitedRetaliate2, LimitedRetaliate3,
                        Retaliate, Retaliate2, Retaliate3)
from .selfsteem import SelfSteem
from .sequence_player import SequencePlayer, ThueMorse, ThueMorseInverse
from .shortmem import ShortMem
from .stalker import Stalker
from .titfortat import (AdaptiveTitForTat, Alexei, AntiTitForTat, Bully,
                        ContriteTitForTat, DynamicTwoTitsForTat, EugineNier,
                        Gradual, HardTitFor2Tats, HardTitForTat, Michaelos,
                        NTitsForMTats, OmegaTFT, RandomTitForTat,
                        SlowTitForTwoTats2, SneakyTitForTat, SpitefulTitForTat,
                        SuspiciousTitForTat, TitFor2Tats, TitForTat,
                        TwoTitsForTat)
from .verybad import VeryBad
from .worse_and_worse import (KnowledgeableWorseAndWorse, WorseAndWorse,
                              WorseAndWorse2, WorseAndWorse3)
from .zero_determinant import (ZDGTFT2, ZDExtort2, ZDExtort2v2, ZDExtort3,
                               ZDExtort4, ZDExtortion, ZDGen2, ZDMischief,
                               ZDSet2)

# Note: Meta* strategies are handled in .__init__.py


all_strategies = [
    Adaptive,
    AdaptiveTitForTat,
    Aggravater,
    Alexei,
    ALLCorALLD,
    Alternator,
    AlternatorHunter,
    AntiCycler,
    AntiTitForTat,
    AON2,
    APavlov2006,
    APavlov2011,
    Appeaser,
    ArrogantQLearner,
    AverageCopier,
    BackStabber,
    BetterAndBetter,
    Black,
    Borufsen,
    Bully,
    BushMosteller,
    Calculator,
    CautiousQLearner,
    Cave,
    Champion,
    Colbert,
    CollectiveStrategy,
    ContriteTitForTat,
    Cooperator,
    CooperatorHunter,
    CycleHunter,
    CyclerCCCCCD,
    CyclerCCCD,
    CyclerCCD,
    CyclerDC,
    CyclerDDC,
    CyclerCCCDCD,
    Darwin,
    Davis,
    DBS,
    Defector,
    DefectorHunter,
    Desperate,
    DelayedAON1,
    DoubleCrosser,
    Doubler,
    DoubleResurrection,
    EasyGo,
    Eatherley,
    EugineNier,
    EventualCycleHunter,
    EvolvedANN,
    EvolvedANN5,
    EvolvedANNNoise05,
    EvolvedFSM4,
    EvolvedFSM16,
    EvolvedFSM16Noise05,
    EvolvedLookerUp1_1_1,
    EvolvedLookerUp2_2_2,
    EvolvedHMM5,
    Feld,
    FirmButFair,
    FoolMeForever,
    FoolMeOnce,
    ForgetfulFoolMeOnce,
    ForgetfulGrudger,
    Forgiver,
    ForgivingTitForTat,
    Fortress3,
    Fortress4,
    GTFT,
    Geller,
    GellerCooperator,
    GellerDefector,
    GeneralSoftGrudger,
    Getzler,
    Gladstein,
    GoByMajority,
    GoByMajority10,
    GoByMajority20,
    GoByMajority40,
    GoByMajority5,
    Golden,
    GraaskampKatzen,
    Gradual,
    GradualKiller,
    Grofman,
    Grudger,
    GrudgerAlternator,
    Grumpy,
    Handshake,
    HardGoByMajority,
    HardGoByMajority10,
    HardGoByMajority20,
    HardGoByMajority40,
    HardGoByMajority5,
    HardProber,
    HardTitFor2Tats,
    HardTitForTat,
    Harrington,
    HesitantQLearner,
    Hopeless,
    Inverse,
    InversePunisher,
    Joss,
    Kluepfel,
    KnowledgeableWorseAndWorse,
    LevelPunisher,
    Leyvraz,
    LimitedRetaliate,
    LimitedRetaliate2,
    LimitedRetaliate3,
    MathConstantHunter,
    NaiveProber,
    MEM2,
    Michaelos,
    Mikkelson,
    MindBender,
    MindController,
    MindReader,
    MindWarper,
    MirrorMindReader,
    MoreGrofman,
    MoreTidemanAndChieruzzi,
    Negation,
    NiceAverageCopier,
    NTitsForMTats,
    Nydegger,
    OmegaTFT,
    OnceBitten,
    OppositeGrudger,
    Pi,
    Predator,
    Prober,
    Prober2,
    Prober3,
    Prober4,
    ProtectedMindReader,
    Pun1,
    PSOGambler1_1_1,
    PSOGambler2_2_2,
    PSOGambler2_2_2_Noise05,
    PSOGamblerMem1,
    Punisher,
    Raider,
    Random,
    RandomHunter,
    RandomTitForTat,
    RemorsefulProber,
    Resurrection,
    Retaliate,
    Retaliate2,
    Retaliate3,
    RevisedDowning,
    RichardHufford,
    Ripoff,
    RiskyQLearner,
    SelfSteem,
    ShortMem,
    Shubik,
    SlowTitForTwoTats2,
    SneakyTitForTat,
    SoftGrudger,
    SoftJoss,
    SolutionB1,
    SolutionB5,
    SpitefulTitForTat,
    Stalker,
    SteinAndRapoport,
    StochasticCooperator,
    StochasticWSLS,
    SuspiciousTitForTat,
    Tester,
    TF1,
    TF2,
    TF3,
    ThueMorse,
    ThueMorseInverse,
    Thumper,
    TidemanAndChieruzzi,
    TitForTat,
    TitFor2Tats,
    Tranquilizer,
    TrickyCooperator,
    TrickyDefector,
    TrickyLevelPunisher,
    Tullock,
    TwoTitsForTat,
    VeryBad,
    Weiner,
    White,
    Willing,
    Winner12,
    Winner21,
    WinShiftLoseStay,
    WinStayLoseShift,
    WmAdams,
    WorseAndWorse,
    WorseAndWorse2,
    WorseAndWorse3,
    Yamachi,
    ZDExtortion,
    ZDExtort2,
    ZDExtort3,
    ZDExtort2v2,
    ZDExtort4,
    ZDGTFT2,
    ZDGen2,
    ZDMem2,
    ZDMischief,
    ZDSet2,
    e,
    DynamicTwoTitsForTat,
]
