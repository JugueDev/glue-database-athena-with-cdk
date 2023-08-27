#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { CdkCodeStack } from '../lib/cdk_code-stack';

const app = new cdk.App();
new CdkCodeStack(app, 'CdkCodeStack');
