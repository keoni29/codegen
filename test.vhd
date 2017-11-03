library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity testip is
Port (
	clk : in std_logic;
	ares : in std_logic;

	$s = [['\td' + dir + '_' + str(a) + ' : std_logic_vector(13 downto 0)' for a in range(20)] for dir in ['in','out']]
	$print ';\n'.join(s[0] + s[1])
	$
);
end testip;

component building_block is
Port (
	clk : in std_logic;
	ares : in std_logic;
	din : in std_logic_vector
);

architecture Behavioral of testip is

begin

$for i in range(20):
$	print 'u%d:building_block ' % i
$	print 'port map ('
$	print '	clk => clk,'
$	print '	ares => ares,'
$	print '	din => din_%d,' % i
$	print '	dout => dout_%d);' %i
$	print ''

end Behavioral;