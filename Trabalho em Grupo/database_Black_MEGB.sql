create database blackmegb;
use blackmegb;

create table Usuarios (id int auto_increment primary key, nome varchar(45), sobrenome varchar(45), nome_exibicao varchar(45), email varchar(45), senha varchar(8));
select * from Usuarios;

create table jogos (id int auto_increment primary key, nome varchar(45));
insert into jogos (nome) values  ('Super Mario World'),('Sonic'), ('Donkey Kong'), ('Mortal Kombat 3'), ('Super Bomberman');
select * from jogos;

#drop database blackmegb;