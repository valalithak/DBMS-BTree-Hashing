#include<bits/stdc++.h>

using namespace std;

long long int bucket_size = 128,num_buckets = 2,curr_count = 0;
long double load_factor = 0.85;

vector<vector<long long int> > linear_hash;

long long int getbinary(long long int n, long long int k)
{
	long long int ans = 0,val = 1,i;
	for(i=0;i<k;i++)
	{
		if(n%2==1)
			ans+=val;
		n = n/2;
		val = val*2;
	}
	return ans;
}

void split()
{
	vector<long long int> a;
	linear_hash.push_back(a);
	num_buckets++;
	long long int newpos,i,pos;
	newpos = num_buckets-1;
	pos = getbinary(newpos,ceil(log2(num_buckets*1.0))-1);
	vector<long long int> b;
	for(i=0;i<linear_hash[pos].size();i++)
	{
		b.push_back(linear_hash[pos][i]);
	}
	if(b.size()>=bucket_size)
		curr_count-=bucket_size;
	else
		curr_count-=b.size();
	linear_hash[pos].clear();
	for(i=0;i<b.size();i++)
	{
		long long int binval = getbinary(b[i],ceil(log2(num_buckets*1.0)));
		if(binval == newpos)
		{
			linear_hash[newpos].push_back(b[i]);
			if(linear_hash[newpos].size()<=bucket_size)
				curr_count++;
		}
		else
		{
			linear_hash[pos].push_back(b[i]);
			if(linear_hash[pos].size()<=bucket_size)
				curr_count++;
		}
	}
}

bool insert(long long int value)
{
	long long int i,bin_num = getbinary(value,ceil(log2(num_buckets*1.0)));
	if(bin_num>=num_buckets)
		bin_num = bin_num >> 1;
	long long int prev_size,curr_size;
	prev_size = linear_hash[bin_num].size();
	for(i=0;i<prev_size;i++)
	{
		if(linear_hash[bin_num][i]==value)
			return false;
	}
	linear_hash[bin_num].push_back(value);
	curr_size = linear_hash[bin_num].size();

	if(curr_size<=bucket_size)
		curr_count++;

	long double curr_load  = (long double)curr_count/((long double)num_buckets*(long double)bucket_size);
	if(curr_load>load_factor)
		split();
	return true;
}

int main(int argc,char* argv[])
{
	long long int i;
	for(i=0;i<num_buckets;i++)
	{
		vector<long long int> a;
		linear_hash.push_back(a);
	}
	string filename = argv[1];
	ifstream infile(filename.c_str());
	long long int value;
	while(infile >> value)
	{
		if(insert(value))
			cout<<value<<endl;
	}
	return 0;
}
