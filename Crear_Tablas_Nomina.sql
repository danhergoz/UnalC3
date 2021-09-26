CREATE TABLE gran_grupo(gg_id INT PRIMARY KEY, gg_codigo VARCHAR(10), gg_nombre VARCHAR(100));
CREATE TABLE subgrupo_principal(sp_id INT PRIMARY KEY, sp_codigo VARCHAR(10), sp_nombre VARCHAR(100), sp_grangrupo INT, FOREIGN KEY (sp_grangrupo) REFERENCES gran_grupo(gg_id));
CREATE TABLE subgrupo(s_id INT PRIMARY KEY, s_codigo VARCHAR(10), s_nombre VARCHAR(100), s_subgrupoprincipal INT, FOREIGN KEY (s_subgrupoprincipal) REFERENCES subgrupo_principal(sp_id));
CREATE TABLE grupo_primario(gp_id INT PRIMARY KEY, gp_codigo VARCHAR(10), gp_nombre VARCHAR(100), gp_subgrupo INT, FOREIGN KEY (gp_subgrupo) REFERENCES subgrupo(s_id));
CREATE TABLE cargo(c_id INT PRIMARY KEY, c_codigo VARCHAR(10), c_nombre VARCHAR(100), c_grupoprimario INT, FOREIGN KEY (c_grupoprimario) REFERENCES grupo_primario(gp_id));