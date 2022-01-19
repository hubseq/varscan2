import json
MODULE = 'varscan2'

mi_template_json = {'module_version': '00.00.00', 'program_name': 'java', 'program_subname': '-jar /VarScan.v2.4.4.jar', 'program_version': '0.7.17', 'compute': {'environment': 'aws', 'language': 'Python', 'language_version': '3.7', 'vcpus': 2, 'memory': 6000}, 'program_arguments': 'mpileup2snp', 'program_input': [{'input_type': 'file', 'input_file_type': 'PILEUP', 'input_position': -1, 'input_prefix': ''}], 'program_output': [{'output_type': 'file', 'output_file_type': 'VCF', 'output_position': -100, 'output_prefix': ''}], 'alternate_inputs': [], 'alternate_outputs': []}
with open(MODULE+'.template.json','w') as fout:
    json.dump(mi_template_json, fout)

io_dryrun_json = {'input': ['s3://npipublicinternal/test/dnaseq_targeted/run_test1/mpileup/dnaseq_test.mpileup.pileup'], 'output': ['s3://npipublicinternal/test/dnaseq_targeted/run_test1/varscan2/dnaseq_test.varscan2.vcf'], 'alternate_inputs': [], 'alternate_outputs': [], 'program_arguments': '', 'sample_id': MODULE+'_test', 'dryrun': ''}
io_json = {'input': ['s3://npipublicinternal/test/dnaseq_targeted/run_test1/mpileup/dnaseq_test.mpileup.pileup'], 'output': ['s3://npipublicinternal/test/dnaseq_targeted/run_test1/varscan2/dnaseq_test.varscan2.vcf'], 'alternate_inputs': [], 'alternate_outputs': [], 'program_arguments': '', 'sample_id': MODULE+'_test'}
io_dryrun_local_json = {'input': ['/Users/jerry/icloud/Documents/ngspipelines/varscan2/test/dnaseq_test.mpileup.pileup'], 'output': ['/Users/jerry/icloud/Documents/ngspipelines/varscan2/testout/dnaseq_test.varscan2.vcf'], 'alternate_inputs': [], 'alternate_outputs': [], 'program_arguments': '', 'sample_id': MODULE+'_test', 'dryrun': ''}
with open(MODULE+'.dryrun_test.io.json','w') as fout:
    json.dump(io_dryrun_json, fout)
with open(MODULE+'.test.io.json','w') as fout:
    json.dump(io_json, fout)
with open(MODULE+'.dryrun_local_test.io.json','w') as fout:
    json.dump(io_dryrun_local_json, fout)

# job info test JSONs                                                                                                        
job_json = {"container_overrides": {"command": ["--module_name", MODULE, "--run_arguments", "s3://npipublicinternal/test/modules/"+MODULE+"/job/"+MODULE+".test.job.json", "--working_dir", "/home/"]}, "jobqueue": "batch_scratch_queue", "jobname": "job_"+MODULE+"_test"}
with open(MODULE+'.test.job.json','w') as fout:
    json.dump(io_json, fout)
