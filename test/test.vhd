library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- Entity with generated interface
entity testip is
Port (
	clk : in std_logic;
	ares : in std_logic;
--<
# This part will cause compiler errors if compiled before running the
# python code.

n_blocks = 12

s = [['\td' + dir + '_' + str(a) + ' : std_logic_vector(13 downto 0)' for a in range(n_blocks)] for dir in ['in','out']]
print ';\n'.join(s[0] + s[1])
-->
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

-- Generated instances
--<
# There are no comment blocks in VHDL, so in order to prevent compiler errors
# you could comment each line of python.

		--for i in range(n_blocks):
		--	print 'u%d:building_block ' % i
		--	print 'port map ('
		--	print '	clk => clk,'
		--	print '	ares => ares,'
		--	print '	din => din_%d,' % i
		--	print '	dout => dout_%d);' %i
		--	print ''
		-->

end Behavioral;