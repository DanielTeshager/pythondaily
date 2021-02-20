#!/usr/bin/env python3
import re
text= """ #BED
        {
            color: #FfFdF8; background-color:#aef;
            font-size: 123px;
            background: -webkit-linear-gradient(top, #f9f9f9, #fff);
        }
        
        Taniel teshager
        daniel teshager
        daniel teshager Daniel
        daniel teshager Daniel
        daniel Wolela
        daniel teshager Daniel
        daniel Wolela


       8 #Cab
        {
            background-color: #ABC;
            border: 2px dashed #fff;
        }

        """
print(text)*******
print(re.findall(r'[/s:]|?#([a-fA-F0-9]+)',text))
