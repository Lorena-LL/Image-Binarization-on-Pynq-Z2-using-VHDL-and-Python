library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity prag_axi4stream32 is
  Port ( 
        m_axis_tdata: in std_logic_vector(31 downto 0);
        m_axis_tkeep: in std_logic_vector(3 downto 0);
        m_axis_tlast: in std_logic;
        m_axis_tready: out std_logic;
        m_axis_tvalid: in std_logic;
        
        m_axis_tdata_out: out std_logic_vector(31 downto 0);
        m_axis_tkeep_out: out std_logic_vector(3 downto 0);
        m_axis_tlast_out: out std_logic;
        m_axis_tready_out: in std_logic;
        m_axis_tvalid_out: out std_logic
        ); 
end prag_axi4stream32;



architecture Behavioral of prag_axi4stream32 is
    signal prag: std_logic_vector(7 downto 0) := x"80";
begin

    m_axis_tdata_out <= (others => '0') when (m_axis_tdata(7 downto 0) < prag) else (others => '1');
    m_axis_tkeep_out <= m_axis_tkeep;
    m_axis_tlast_out <= m_axis_tlast;
    m_axis_tready <= m_axis_tready_out;
    m_axis_tvalid_out <= m_axis_tvalid;
    
end Behavioral;
