/*
커피 한 잔 과 쿼리 한 줄의 여유^^
*/

USE myshop2019;

-- 1) 쿼리 #1

select customer_name as 고객명,
	   phone as 전화번호,
	   repeat('▒', cast(point /10000 as unsigned)) as 포인트
	from customer
    where city in ('대전', '인천')
		  and point > 0
	order by point desc;
    
-- 2) 쿼리 #2

-- 기본 집계
select city as 지역,
	   sum(point) as 포인트
	from customer
    group by city;

-- 고급 집계(피벗, 크로스탭)
select city as 지역,
	   sum(if(gender='F', point, 0)) as 여자,
       sum(if(gender='M', point, 0)) as 남자,
	   sum(point) as 전체포인트
	from customer
    group by city;
    
    -- 고급 집계(피벗, 크로스탭)
select gender as 성별,
	   sum(if(city='서울', point, 0)) as 서울,
       sum(if(city='부산', point, 0)) as 부산,
       sum(if(city='광주', point, 0)) as 광주,
       sum(if(city='대구', point, 0)) as 대구,
       sum(if(city='인천', point, 0)) as 인천,
	   sum(point) as 전체포인트
	from customer
    group by gender;
    
