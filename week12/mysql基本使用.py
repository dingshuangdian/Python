# Create by dingshuangdian


'''
desc user; //查看表结构

select *from user\G; //查看表数据

mysqladmin -u root password "123"；//创建密码

ps -ef:查看所有进程

ps -ef |grep mysql ：查看mysql进程

mysql ./mysqld_safe & :启动

./mysqladmin -u root -p shutdown :关闭mysql service

创建用户：
grant ALL on test.* to 'uroot'@'%' identified by 'qw123456';

创建数据库(带字符集)：
create database test charset "utf8";

删除数据库

drop database test;

创建数据表
create table table_name(column_name coumn_type);
create table student(id int auto_increment,
    -> name char(32) not null,
    -> age int not null,
    -> register_date date not null,
    -> primary key(id));

表插入数据：
insert into student (name,age,register_date) values("a",3,"2018-08-01")

查询数据:
select *from student limit 2 offset 2;去掉前两条

select *from student where id=4;
模糊查询：
select *from student where id=4 like "";

修改数据:

update student set name="a",age=33 where id=4;

delete  from student where name="a"

排序：








'''