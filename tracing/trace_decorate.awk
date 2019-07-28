
function  BLACK(x)             { return "\033[30m"   x "\033[0m" }
function  RED(x)               { return "\033[31m"   x "\033[0m" }
function  GREEN(x)             { return "\033[32m"   x "\033[0m" }
function  YELLOW(x)            { return "\033[33m"   x "\033[0m" }
function  BLUE(x)              { return "\033[34m"   x "\033[0m" }
function  MAGENTA(x)           { return "\033[35m"   x "\033[0m" }
function  CYAN(x)              { return "\033[36m"   x "\033[0m" }
function  WHITE(x)             { return "\033[37m"   x "\033[0m" }
function  BRIGHT_BLACK(x)      { return "\033[90m"   x "\033[0m" }
function  BRIGHT_RED(x)        { return "\033[91m"   x "\033[0m" }
function  BRIGHT_GREEN(x)      { return "\033[92m"   x "\033[0m" }
function  BRIGHT_YELLOW(x)     { return "\033[93m"   x "\033[0m" }
function  BRIGHT_BLUE(x)       { return "\033[94m"   x "\033[0m" }
function  BRIGHT_MAGENTA(x)    { return "\033[95m"   x "\033[0m" }
function  BRIGHT_CYAN(x)       { return "\033[96m"   x "\033[0m" }
function  BRIGHT_WHITE(x)      { return "\033[97m"   x "\033[0m" }
function  BG_BLACK(x)          { return "\033[40m"   x "\033[0m" }
function  BG_RED(x)            { return "\033[41m"   x "\033[0m" }
function  BG_GREEN(x)          { return "\033[42m"   x "\033[0m" }
function  BG_YELLOW(x)         { return "\033[43m"   x "\033[0m" }
function  BG_BLUE(x)           { return "\033[44m"   x "\033[0m" }
function  BG_MAGENTA(x)        { return "\033[45m"   x "\033[0m" }
function  BG_CYAN(x)           { return "\033[46m"   x "\033[0m" }
function  BG_WHITE(x)          { return "\033[47m"   x "\033[0m" }
function  BG_BRIGHT_BLACK(x)   { return "\033[100m"  x "\033[0m" }
function  BG_BRIGHT_RED(x)     { return "\033[101m"  x "\033[0m" }
function  BG_BRIGHT_GREEN(x)   { return "\033[102m"  x "\033[0m" }
function  BG_BRIGHT_YELLOW(x)  { return "\033[103m"  x "\033[0m" }
function  BG_BRIGHT_BLUE(x)    { return "\033[104m"  x "\033[0m" }
function  BG_BRIGHT_MAGENTA(x) { return "\033[105m"  x "\033[0m" }
function  BG_BRIGHT_CYAN(x)    { return "\033[106m"  x "\033[0m" }
function  BG_BRIGHT_WHITE(x)   { return "\033[107m"  x "\033[0m" }

/wm8741_startup/  { $0 = BG_BLUE($0)                             }
/wm8741_mute/     { $0 = BG_MAGENTA($0)                          }
/\/\* clk_*/      { $0 = BRIGHT_BLACK($0)                        }
/\/\* i2c_*/      { $0 = BRIGHT_GREEN($0)                        }
/\/\* gpio_*/     { $0 = BRIGHT_RED($0)                          }
/pll/             { $0 = BLACK($0); $0 = BG_YELLOW($0)           }
1

# vim: ts=2 sw=2 et
