State-Pattern
=============

GumBallMachine - State Pattern implementation


''''''''''''''''                   ''''''''''''''''''''      insert quarter
|SoldOutState  |               --> | NoQuarterState    |---------------------
''''''''''''''''              |     '''''''''''''''''''                      |
        ^                     |              ^                               |
        |                     |              |                               |
        |                     |              |                               |
         --------- -----------               |                               |
       dispense=0 |  dispense > 0            |                               |
                  |                          |                               |
                  |                          |                               v
           '''''''''''''''''''               |                      ''''''''''''''''''''
           |SoldState        |               -----------------------|HasQuarter        |
           '''''''''''''''''''                eject quarter         ''''''''''''''''''''
                  ^                                                          |
                  |                                                          |
                   ----------------------------------------------------------
                                      turn crank
